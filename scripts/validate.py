#!/usr/bin/env python3
"""Deterministic repository checks for Cognitive Agent Skills v2."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "cognitive-agent-skills"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
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


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)

    def load_json(self, path: Path) -> object:
        self.require(path.is_file(), f"missing JSON file: {path.relative_to(ROOT)}")
        if not path.is_file():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
            return {}

    def validate_manifest(self) -> None:
        data = self.load_json(MANIFEST)
        if not isinstance(data, dict):
            self.errors.append("plugin manifest must be a JSON object")
            return

        allowed_top = {
            "name", "version", "description", "author", "homepage", "repository",
            "keywords", "skills", "interface",
        }
        self.require(set(data) == allowed_top, f"unexpected or missing plugin fields: {sorted(set(data) ^ allowed_top)}")

        self.require(data.get("name") == PLUGIN.name, "plugin name must match its directory")
        version = data.get("version")
        self.require(
            isinstance(version, str)
            and re.fullmatch(r"0|[1-9]\d*\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", version) is not None,
            "plugin version must be strict semantic versioning",
        )
        self.require(isinstance(data.get("description"), str) and bool(data["description"].strip()), "plugin description is required")

        author = data.get("author")
        interface = data.get("interface")
        self.require(isinstance(author, dict) and bool(author.get("name")), "author.name is required")
        self.require(isinstance(interface, dict), "interface object is required")
        if isinstance(author, dict):
            self.require(set(author) == {"name", "url"}, "author must contain exactly name and url")
            self.require(self.is_https_url(author.get("url")), "author.url must be an absolute HTTPS URL")
        self.require(self.is_https_url(data.get("homepage")), "homepage must be an absolute HTTPS URL")
        self.require(self.is_https_url(data.get("repository")), "repository must be an absolute HTTPS URL")
        keywords = data.get("keywords")
        self.require(isinstance(keywords, list) and all(isinstance(item, str) and item for item in keywords), "keywords must be a non-empty string list")
        if isinstance(interface, dict):
            allowed_interface = {
                "displayName", "shortDescription", "longDescription", "developerName",
                "category", "capabilities", "websiteURL", "defaultPrompt",
            }
            self.require(set(interface) == allowed_interface, f"unexpected or missing interface fields: {sorted(set(interface) ^ allowed_interface)}")
            for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
                self.require(isinstance(interface.get(field), str) and bool(interface[field].strip()), f"interface.{field} is required")
            if isinstance(author, dict):
                self.require(interface.get("developerName") == author.get("name"), "developerName must match author.name")
            self.require(self.is_https_url(interface.get("websiteURL")), "interface.websiteURL must be an absolute HTTPS URL")
            capabilities = interface.get("capabilities")
            self.require(isinstance(capabilities, list) and all(isinstance(item, str) and item for item in capabilities), "capabilities must be a non-empty string list")
            prompts = interface.get("defaultPrompt")
            self.require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, "defaultPrompt must contain one to three entries")
            if isinstance(prompts, list):
                self.require(all(isinstance(item, str) and len(item) <= 128 for item in prompts), "defaultPrompt entries must be strings of at most 128 characters")

        skills_path = data.get("skills")
        self.require(skills_path == "./skills/", "manifest skills path must be ./skills/")
        self.require((PLUGIN / "skills").is_dir(), "manifest skills directory does not exist")
        self.require("mcpServers" not in data and "apps" not in data, "skills-only plugin must not declare MCP or app configuration")

    @staticmethod
    def is_https_url(value: object) -> bool:
        if not isinstance(value, str):
            return False
        parsed = urlparse(value)
        return parsed.scheme == "https" and bool(parsed.netloc)

    def parse_frontmatter(self, path: Path) -> dict[str, str]:
        self.require(path.is_file(), f"missing Markdown file: {path.relative_to(ROOT)}")
        if not path.is_file():
            return {}
        text = path.read_text(encoding="utf-8")
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
            result[key.strip()] = value.strip().strip('"\'')
        return result

    def validate_skill(self) -> None:
        frontmatter = self.parse_frontmatter(SKILL_MD)
        self.require(frontmatter.get("name") == SKILL.name, "skill name must match its directory")
        self.require(set(frontmatter) == {"name", "description"}, "SKILL.md frontmatter must contain only name and description")
        description = frontmatter.get("description", "")
        self.require("Lite" in description and "High Precision" in description, "skill description must expose routing scope")
        self.require("do not use" in description, "skill description must preserve the simple-execution boundary")

        refs = SKILL / "references"
        present = {path.name for path in refs.glob("*.md")}
        self.require(present == REQUIRED_REFERENCES, f"protocol reference inventory mismatch: {sorted(present)}")

        yaml_text = OPENAI_YAML.read_text(encoding="utf-8") if OPENAI_YAML.is_file() else ""
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

        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
        markdown_files = ([SKILL_MD] if SKILL_MD.is_file() else []) + sorted(refs.glob("*.md"))
        for markdown in markdown_files:
            text = markdown.read_text(encoding="utf-8")
            self.require(not any(token in text for token in PLACEHOLDERS), f"unfinished placeholder in {markdown.relative_to(ROOT)}")
            for target in link_pattern.findall(text):
                resolved = (markdown.parent / target).resolve()
                self.require(resolved.is_file(), f"broken Markdown link in {markdown.relative_to(ROOT)}: {target}")

        legacy = ROOT / "skills"
        present_legacy = {path.name for path in legacy.iterdir()} if legacy.is_dir() else set()
        self.require(not (present_legacy & RETIRED_SKILLS), f"retired v1 skill directories remain: {sorted(present_legacy & RETIRED_SKILLS)}")

    def validate_evals(self) -> None:
        data = self.load_json(EVALS)
        if not isinstance(data, dict):
            self.errors.append("evaluation file must be a JSON object")
            return
        self.require(data.get("schema_version") == 1, "unsupported evaluation schema_version")
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
            self.require(isinstance(case_id, str) and bool(case_id), f"evaluation case {index} needs an id")
            if isinstance(case_id, str):
                self.require(case_id not in ids, f"duplicate evaluation id: {case_id}")
                ids.add(case_id)
            self.require(isinstance(case.get("prompt"), str) and bool(case["prompt"].strip()), f"evaluation case {case_id} needs a prompt")
            self.require(isinstance(case.get("should_trigger"), bool), f"evaluation case {case_id} needs should_trigger")
            mode = case.get("expected_mode")
            self.require(mode in ALLOWED_MODES, f"evaluation case {case_id} has invalid expected_mode")
            self.require(isinstance(case.get("rationale"), str) and bool(case["rationale"].strip()), f"evaluation case {case_id} needs a rationale")
            must_observe = case.get("must_observe", [])
            self.require(isinstance(must_observe, list) and all(isinstance(item, str) and item for item in must_observe), f"evaluation case {case_id} has invalid must_observe")
            modes.add(mode)
            if isinstance(case.get("should_trigger"), bool):
                triggers.add(case["should_trigger"])

        self.require({"lite", "standard", "high-precision", "mixed", None} <= modes, "evaluation cases must cover every mode and a non-trigger")
        self.require(triggers == {True, False}, "evaluation cases must cover trigger and non-trigger behavior")
        self.require(any("overrides-lite" in case_id for case_id in ids), "a safety override regression case is required")

    def validate_repository_text(self) -> None:
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py"}:
                continue
            text = path.read_text(encoding="utf-8")
            self.require(not any(token in text for token in PLACEHOLDERS), f"unfinished placeholder in {path.relative_to(ROOT)}")
            if path.suffix.lower() == ".md":
                for target in link_pattern.findall(text):
                    if target.startswith(("https://", "http://", "#")):
                        continue
                    clean_target = target.split("#", 1)[0]
                    self.require((path.parent / clean_target).resolve().exists(), f"broken repository link in {path.relative_to(ROOT)}: {target}")

    def run(self) -> int:
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
