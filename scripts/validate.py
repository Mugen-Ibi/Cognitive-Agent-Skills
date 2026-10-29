#!/usr/bin/env python3
"""Deterministic repository checks for Cognitive Agent Skills."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "cognitive-agent-skills"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILL = PLUGIN / "skills" / "cognitive-router"
SKILL_MD = SKILL / "SKILL.md"
OPENAI_YAML = SKILL / "agents" / "openai.yaml"
EVALS = ROOT / "evals" / "cases.json"

REQUIRED_REFERENCES = {
    "routing.md",
    "lite.md",
    "standard.md",
    "high-precision.md",
    "evidence.md",
}
RETIRED_SKILLS = {
    "cognitive-lite",
    "cognitive-standard",
    "cognitive-high-precision",
    "cognitive-router",
}
ALLOWED_MODES = {"lite", "standard", "high-precision", "mixed", None}
PLACEHOLDERS = ("[" + "TODO", "TODO" + ":")
IGNORED_DIRECTORIES = {".git", ".venv", "venv", "__pycache__", "node_modules", ".pytest_cache"}
# SemVer 2.0.0: core/numeric prerelease identifiers have no leading zeroes;
# build identifiers may. Use ASCII digits, not Python's Unicode-aware \d.
NUMERIC_IDENTIFIER = r"(?:0|[1-9][0-9]*)"
PRERELEASE_IDENTIFIER = rf"(?:{NUMERIC_IDENTIFIER}|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
SEMVER = re.compile(
    rf"{NUMERIC_IDENTIFIER}\.{NUMERIC_IDENTIFIER}\.{NUMERIC_IDENTIFIER}"
    rf"(?:-{PRERELEASE_IDENTIFIER}(?:\.{PRERELEASE_IDENTIFIER})*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)


def unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)

    def read_text(self, path: Path) -> str | None:
        """Collect bad-input diagnostics without reading outside the repository."""
        try:
            if not path.resolve().is_relative_to(ROOT.resolve()):
                self.errors.append(f"file resolves outside repository: {path.relative_to(ROOT)}")
                return None
            if not path.is_file():
                self.errors.append(f"not a regular file: {path.relative_to(ROOT)}")
                return None
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError, RuntimeError) as exc:
            self.errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
            return None

    def load_json(self, path: Path) -> object:
        self.require(path.is_file(), f"missing JSON file: {path.relative_to(ROOT)}")
        if not path.is_file():
            return {}
        text = self.read_text(path)
        if text is None:
            return {}
        try:
            return json.loads(text, object_pairs_hook=unique_json_object)
        except ValueError as exc:
            self.errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
            return {}

    def validate_manifest(self) -> None:
        data = self.load_json(MANIFEST)
        if not isinstance(data, dict):
            self.errors.append("plugin manifest must be a JSON object")
            return

        required_top = {
            "name", "version", "description", "author", "homepage", "repository",
            "license", "keywords", "skills", "interface",
        }
        allowed_top = required_top | {"mcpServers", "apps"}
        self.require(required_top <= set(data), f"missing plugin fields: {sorted(required_top - set(data))}")
        self.require(set(data) <= allowed_top, f"unsupported plugin fields: {sorted(set(data) - allowed_top)}")

        self.require(data.get("name") == PLUGIN.name, "plugin name must match its directory")
        version = data.get("version")
        self.require(
            isinstance(version, str)
            and SEMVER.fullmatch(version) is not None,
            "plugin version must be strict semantic versioning",
        )
        self.require(isinstance(data.get("description"), str) and bool(data["description"].strip()), "plugin description is required")

        author = data.get("author")
        interface = data.get("interface")
        self.require(isinstance(author, dict) and isinstance(author.get("name"), str) and bool(author["name"].strip()), "author.name is required")
        self.require(isinstance(interface, dict), "interface object is required")
        if isinstance(author, dict):
            self.require(set(author) == {"name", "url"}, "author must contain exactly name and url")
            self.require(self.is_https_url(author.get("url")), "author.url must be an absolute HTTPS URL")
        self.require(self.is_https_url(data.get("homepage")), "homepage must be an absolute HTTPS URL")
        self.require(self.is_https_url(data.get("repository")), "repository must be an absolute HTTPS URL")
        self.require(data.get("license") == "Apache-2.0", "plugin license must be Apache-2.0")
        keywords = data.get("keywords")
        self.require(isinstance(keywords, list) and bool(keywords) and all(isinstance(item, str) and item.strip() for item in keywords), "keywords must be a non-empty string list")
        if isinstance(interface, dict):
            required_interface = {
                "displayName", "shortDescription", "longDescription", "developerName",
                "category", "capabilities", "websiteURL", "defaultPrompt",
            }
            allowed_interface = required_interface | {
                "privacyPolicyURL", "termsOfServiceURL", "brandColor", "composerIcon",
                "logo", "logoDark", "screenshots",
            }
            self.require(required_interface <= set(interface), f"missing interface fields: {sorted(required_interface - set(interface))}")
            self.require(set(interface) <= allowed_interface, f"unsupported interface fields: {sorted(set(interface) - allowed_interface)}")
            for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
                value = interface.get(field)
                self.require(isinstance(value, str) and bool(value.strip()), f"interface.{field} is required")
            if isinstance(author, dict):
                self.require(interface.get("developerName") == author.get("name"), "developerName must match author.name")
            self.require(self.is_https_url(interface.get("websiteURL")), "interface.websiteURL must be an absolute HTTPS URL")
            capabilities = interface.get("capabilities")
            self.require(isinstance(capabilities, list) and bool(capabilities) and all(isinstance(item, str) and item.strip() for item in capabilities), "capabilities must be a non-empty string list")
            prompts = interface.get("defaultPrompt")
            self.require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, "defaultPrompt must contain one to three entries")
            if isinstance(prompts, list):
                self.require(all(isinstance(item, str) and bool(item.strip()) and len(item) <= 128 for item in prompts), "defaultPrompt entries must be non-blank strings of at most 128 characters")

        skills_path = data.get("skills")
        self.require(skills_path == "./skills/", "manifest skills path must be ./skills/")
        self.require((PLUGIN / "skills").is_dir(), "manifest skills directory does not exist")
        self.require("mcpServers" not in data and "apps" not in data, "skills-only plugin must not declare MCP or app configuration")

    def validate_marketplace(self) -> None:
        data = self.load_json(MARKETPLACE)
        if not isinstance(data, dict):
            self.errors.append("marketplace manifest must be a JSON object")
            return

        self.require(data.get("name") == "cognitive-agent-skills", "unexpected marketplace name")
        interface = data.get("interface")
        self.require(
            isinstance(interface, dict) and interface.get("displayName") == "Cognitive Agent Skills",
            "marketplace interface.displayName must be Cognitive Agent Skills",
        )
        plugins = data.get("plugins")
        self.require(isinstance(plugins, list) and len(plugins) == 1, "marketplace must contain exactly one plugin")
        if not isinstance(plugins, list) or len(plugins) != 1:
            return
        self.require(isinstance(plugins[0], dict), "marketplace plugin entry must be an object")
        if not isinstance(plugins[0], dict):
            return

        entry = plugins[0]
        self.require(entry.get("name") == PLUGIN.name, "marketplace plugin name must match plugin directory")
        source = entry.get("source")
        self.require(
            source == {"source": "local", "path": "./plugins/cognitive-agent-skills"},
            "marketplace source must point to ./plugins/cognitive-agent-skills",
        )
        self.require(
            entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "marketplace policy must declare AVAILABLE and ON_INSTALL",
        )
        self.require(entry.get("category") == "Productivity", "marketplace category must be Productivity")
        self.require(MANIFEST.is_file(), "marketplace source does not contain .codex-plugin/plugin.json")

    @staticmethod
    def is_https_url(value: object) -> bool:
        if not isinstance(value, str) or any(char.isspace() or ord(char) < 32 or ord(char) == 127 for char in value):
            return False
        try:
            parsed = urlparse(value)
            # Accessing port also validates numeric syntax and its allowed range.
            parsed.port
            return parsed.scheme == "https" and bool(parsed.hostname) and parsed.username is None and parsed.password is None
        except ValueError:
            return False

    def parse_frontmatter(self, path: Path) -> dict[str, str]:
        self.require(path.is_file(), f"missing Markdown file: {path.relative_to(ROOT)}")
        if not path.is_file():
            return {}
        text = self.read_text(path)
        if text is None:
            return {}
        match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
        self.require(match is not None, f"missing YAML frontmatter: {path.relative_to(ROOT)}")
        if match is None:
            return {}
        result: dict[str, str] = {}
        for line in match.group(1).splitlines():
            if ":" not in line:
                self.errors.append(f"invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            self.require(key not in result, f"duplicate frontmatter key in {path.relative_to(ROOT)}: {key}")
            result[key] = value.strip().strip('"\'')
        return result

    def validate_skill(self) -> None:
        frontmatter = self.parse_frontmatter(SKILL_MD)
        self.require(frontmatter.get("name") == SKILL.name, "skill name must match its directory")
        self.require(set(frontmatter) == {"name", "description"}, "SKILL.md frontmatter must contain only name and description")
        description = frontmatter.get("description", "")
        self.require(bool(description.strip()) and len(description) <= 1024, "skill description must be non-empty and at most 1024 characters")

        refs = SKILL / "references"
        present = {path.name for path in refs.glob("*.md")}
        self.require(present == REQUIRED_REFERENCES, f"protocol reference inventory mismatch: {sorted(present)}")

        yaml_text = self.read_text(OPENAI_YAML) if OPENAI_YAML.is_file() else ""
        self.require(bool(yaml_text), "agents/openai.yaml is required")
        expected_yaml = (
            'interface:\n'
            '  display_name: "Cognitive Router"\n'
            '  short_description: "Match reasoning rigor to each task"\n'
            '  default_prompt: "Use $cognitive-router to analyze this request at the right depth."\n'
            '\n'
            'policy:\n'
            '  allow_implicit_invocation: true\n'
        )
        self.require(yaml_text == expected_yaml, "agents/openai.yaml must match the validated UI and invocation policy schema")

        markdown_files = ([SKILL_MD] if SKILL_MD.is_file() else []) + sorted(refs.glob("*.md"))
        for markdown in markdown_files:
            text = self.read_text(markdown)
            if text is None:
                continue
            self.require(not any(token in text for token in PLACEHOLDERS), f"unfinished placeholder in {markdown.relative_to(ROOT)}")
            self.validate_local_links(markdown, text, SKILL)

        legacy = ROOT / "skills"
        present_legacy = {path.name for path in legacy.iterdir()} if legacy.is_dir() else set()
        self.require(not (present_legacy & RETIRED_SKILLS), f"retired v1 skill directories remain: {sorted(present_legacy & RETIRED_SKILLS)}")

    def validate_evals(self) -> None:
        data = self.load_json(EVALS)
        if not isinstance(data, dict):
            self.errors.append("evaluation file must be a JSON object")
            return
        self.require(type(data.get("schema_version")) is int and data["schema_version"] == 1, "unsupported evaluation schema_version")
        cases = data.get("cases")
        self.require(isinstance(cases, list) and len(cases) >= 10, "at least ten evaluation cases are required")
        if not isinstance(cases, list):
            return

        ids: set[str] = set()
        modes: set[str | None] = set()
        triggers: set[bool] = set()
        for index, case in enumerate(cases):
            self.require(isinstance(case, dict), f"evaluation case {index} must be an object")
            if not isinstance(case, dict):
                continue
            case_id = case.get("id")
            self.require(isinstance(case_id, str) and bool(case_id.strip()), f"evaluation case {index} needs an id")
            if isinstance(case_id, str):
                self.require(case_id not in ids, f"duplicate evaluation id: {case_id}")
                ids.add(case_id)
            self.require(isinstance(case.get("prompt"), str) and bool(case["prompt"].strip()), f"evaluation case {case_id} needs a prompt")
            self.require(isinstance(case.get("should_trigger"), bool), f"evaluation case {case_id} needs should_trigger")
            mode = case.get("expected_mode")
            valid_mode = "expected_mode" in case and (mode is None or isinstance(mode, str) and mode in ALLOWED_MODES)
            self.require(valid_mode, f"evaluation case {case_id} has invalid or missing expected_mode")
            if valid_mode:
                modes.add(mode)
                if isinstance(case.get("should_trigger"), bool):
                    self.require(case["should_trigger"] == (mode is not None), f"evaluation case {case_id} expected_mode must agree with should_trigger")
            self.require(isinstance(case.get("rationale"), str) and bool(case["rationale"].strip()), f"evaluation case {case_id} needs a rationale")
            must_observe = case.get("must_observe", [])
            self.require(isinstance(must_observe, list) and all(isinstance(item, str) and item.strip() for item in must_observe), f"evaluation case {case_id} has invalid must_observe")
            if isinstance(case.get("should_trigger"), bool):
                triggers.add(case["should_trigger"])

        self.require({"lite", "standard", "high-precision", "mixed", None} <= modes, "evaluation cases must cover every mode and a non-trigger")
        self.require(triggers == {True, False}, "evaluation cases must cover trigger and non-trigger behavior")
        self.require(any("overrides-lite" in case_id for case_id in ids), "a safety override regression case is required")

    def validate_local_links(self, path: Path, text: str, scope: Path) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for target in link_pattern.findall(text):
            if target.startswith(("https://", "http://", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            try:
                resolved = (path.parent / clean_target).resolve()
                self.require(resolved.is_relative_to(scope.resolve()), f"link outside package in {path.relative_to(ROOT)}: {target}")
                self.require(resolved.is_file() if clean_target.lower().endswith(".md") else resolved.exists(), f"broken repository link in {path.relative_to(ROOT)}: {target}")
            except (OSError, RuntimeError, ValueError) as exc:
                self.errors.append(f"invalid repository link in {path.relative_to(ROOT)}: {target}: {exc}")

    def validate_repository_text(self) -> None:
        def walk_error(error: OSError) -> None:
            self.errors.append(f"cannot scan repository directory: {error}")

        for directory, directories, filenames in os.walk(ROOT, onerror=walk_error):
            directories[:] = sorted(name for name in directories if name not in IGNORED_DIRECTORIES)
            for filename in sorted(filenames):
                path = Path(directory) / filename
                if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py"}:
                    continue
                text = self.read_text(path)
                if text is None:
                    continue
                self.require(not any(token in text for token in PLACEHOLDERS), f"unfinished placeholder in {path.relative_to(ROOT)}")
                if path.suffix.lower() == ".md":
                    self.validate_local_links(path, text, ROOT)

    def run(self) -> int:
        self.validate_marketplace()
        self.validate_manifest()
        self.validate_skill()
        self.validate_evals()
        self.validate_repository_text()
        if self.errors:
            print("Validation failed:")
            for error in self.errors:
                print(f"- {error}")
            return 1
        print("Validation passed: plugin, skill, references, metadata, and eval cases are consistent.")
        return 0


if __name__ == "__main__":
    sys.exit(Validator().run())
