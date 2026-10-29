"""Dependency-free regression checks for malformed package input."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import validate


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = validate.Validator()
        self.manifest = json.loads(validate.MANIFEST.read_text(encoding="utf-8"))
        self.marketplace = json.loads(validate.MARKETPLACE.read_text(encoding="utf-8"))
        self.evals = json.loads(validate.EVALS.read_text(encoding="utf-8"))

    def check_manifest(self, data: object) -> list[str]:
        validator = validate.Validator()
        with patch.object(validator, "load_json", return_value=data):
            validator.validate_manifest()
        return validator.errors

    def check_evals(self, data: object) -> list[str]:
        validator = validate.Validator()
        with patch.object(validator, "load_json", return_value=data):
            validator.validate_evals()
        return validator.errors

    def test_current_repository_passes(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.validator.run(), 0)
        self.assertEqual(self.validator.errors, [])

    def test_valid_semver_versions(self) -> None:
        for version in ("0.0.0", "0.1.0", "1.2.3", "1.0.0-alpha.1", "1.0.0-0.3.7",
                        "1.0.0-x-y-z.--", "1.0.0+001", "1.0.0-beta+exp.sha.5114f85"):
            with self.subTest(version=version):
                self.manifest["version"] = version
                self.assertEqual(self.check_manifest(self.manifest), [])

    def test_invalid_semver_versions(self) -> None:
        for version in ("0", "1", "1.0", "01.2.3", "1.02.3", "1.2.03", "1.0.0-01",
                        "1.0.0-alpha..1", "1.0.0-.", "1.0.0+build..1", "1.0.0+.",
                        "1.2.3\n", "1.٢.3", "v1.2.3", None, [], {}):
            with self.subTest(version=version):
                self.manifest["version"] = version
                self.assertTrue(any("semantic versioning" in error for error in self.check_manifest(self.manifest)))

    def test_empty_or_blank_manifest_lists_fail(self) -> None:
        for field in ("keywords", "capabilities"):
            for value in ([], [""], ["   "], [7], "not a list", None):
                with self.subTest(field=field, value=value):
                    data = copy.deepcopy(self.manifest)
                    target = data if field == "keywords" else data["interface"]
                    target[field] = value
                    self.assertTrue(any(field in error for error in self.check_manifest(data)))

    def test_blank_default_prompts_fail(self) -> None:
        for value in ([""], ["   "], ["a" * 129], [1], []):
            with self.subTest(value=value):
                self.manifest["interface"]["defaultPrompt"] = value
                self.assertTrue(any("defaultPrompt" in error for error in self.check_manifest(self.manifest)))

    def test_author_name_must_be_nonblank_string(self) -> None:
        for value in (" ", 123, [], None):
            with self.subTest(value=value):
                self.manifest["author"]["name"] = value
                self.assertTrue(any("author.name is required" in error for error in self.check_manifest(self.manifest)))

    def test_valid_https_urls(self) -> None:
        for value in ("https://example.com", "https://example.com:443/path?a=b#c", "https://[::1]/"):
            with self.subTest(value=value):
                self.assertTrue(validate.Validator.is_https_url(value))

    def test_invalid_https_urls_do_not_raise(self) -> None:
        for value in ("http://example.com", "https://", "https://[", "https://:443", "https://example.com:bad",
                      "https://example.com:99999", "https://example .com", "https://exa\nmple.com", " https://example.com",
                      "https://user:secret@example.com", None, {}):
            with self.subTest(value=value):
                self.assertFalse(validate.Validator.is_https_url(value))

    def test_marketplace_entry_must_be_an_object(self) -> None:
        for entry in (42, None, "plugin", []):
            with self.subTest(entry=entry):
                self.marketplace["plugins"] = [entry]
                validator = validate.Validator()
                with patch.object(validator, "load_json", return_value=self.marketplace):
                    validator.validate_marketplace()
                self.assertTrue(any("object" in error for error in validator.errors))

    def test_json_duplicate_keys_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            path = Path(directory) / "test.json"
            path.write_text('{"name":"first","name":"second"}', encoding="utf-8")
            self.validator.load_json(path)
        self.assertTrue(any("duplicate" in error for error in self.validator.errors))

    def test_invalid_json_encoding_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            path = Path(directory) / "test.json"
            path.write_bytes(b'\xff')
            self.validator.load_json(path)
        self.assertTrue(self.validator.errors)

    def test_duplicate_frontmatter_keys_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            path = Path(directory) / "SKILL.md"
            path.write_text('---\nname: first\nname: second\ndescription: test\n---\n', encoding="utf-8")
            self.validator.parse_frontmatter(path)
        self.assertTrue(any("duplicate" in error for error in self.validator.errors))

    def test_invalid_frontmatter_encoding_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            path = Path(directory) / "SKILL.md"
            path.write_bytes(b'\xff')
            self.validator.parse_frontmatter(path)
        self.assertTrue(self.validator.errors)

    def test_malformed_modes_are_reported_without_crashing(self) -> None:
        for mode in ([], {}, True, 1, "unknown"):
            with self.subTest(mode=mode):
                self.evals["cases"][0]["expected_mode"] = mode
                self.assertTrue(any("expected_mode" in error for error in self.check_evals(self.evals)))

    def test_expected_mode_is_required_even_for_non_trigger(self) -> None:
        case = next(case for case in self.evals["cases"] if not case["should_trigger"])
        del case["expected_mode"]
        self.assertTrue(any("expected_mode" in error for error in self.check_evals(self.evals)))

    def test_mode_and_trigger_must_be_consistent(self) -> None:
        for trigger, mode in ((False, "lite"), (True, None)):
            with self.subTest(trigger=trigger, mode=mode):
                self.evals["cases"][0].update(should_trigger=trigger, expected_mode=mode)
                self.assertTrue(any("expected_mode" in error for error in self.check_evals(self.evals)))

    def test_boolean_schema_version_is_not_integer_one(self) -> None:
        self.evals["schema_version"] = True
        self.assertTrue(any("schema_version" in error for error in self.check_evals(self.evals)))

    def test_blank_evaluation_fields_fail(self) -> None:
        for field in ("id", "prompt", "rationale"):
            with self.subTest(field=field):
                data = copy.deepcopy(self.evals)
                data["cases"][0][field] = " "
                self.assertTrue(any(field in error for error in self.check_evals(data)))
        self.evals["cases"][0]["must_observe"] = [" "]
        self.assertTrue(any("must_observe" in error for error in self.check_evals(self.evals)))

    def test_invalid_repository_text_encoding_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            (Path(directory) / "test.md").write_bytes(b'\xff')
            self.validator.validate_repository_text()
        self.assertTrue(self.validator.errors)

    def test_local_links_cannot_escape_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            (Path(directory) / "outside.md").write_text("outside", encoding="utf-8")
            (root / "readme.md").write_text("[outside](../outside.md)", encoding="utf-8")
            with patch.object(validate, "ROOT", root):
                self.validator.validate_repository_text()
        self.assertTrue(any("outside" in error for error in self.validator.errors))

    def test_existing_local_links_and_fragments_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            root = Path(directory)
            (root / "target.md").write_text("# Target", encoding="utf-8")
            (root / "readme.md").write_text(
                "[target](target.md#target) [self](#self) [web](https://example.com/guide.md)",
                encoding="utf-8",
            )
            self.validator.validate_repository_text()
        self.assertEqual(self.validator.errors, [])

    def test_markdown_link_cannot_target_a_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            root = Path(directory)
            (root / "guide.md").mkdir()
            self.validator.validate_local_links(root / "SKILL.md", "[guide](guide.md#section)", root)
        self.assertTrue(any("broken repository link" in error for error in self.validator.errors))

    def test_repository_directory_links_remain_supported(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            root = Path(directory)
            (root / "docs").mkdir()
            self.validator.validate_local_links(root / "README.md", "[docs](docs/)", root)
        self.assertEqual(self.validator.errors, [])

    def test_skill_links_cannot_escape_standalone_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            root = Path(directory)
            skill = root / "skill"
            skill.mkdir()
            (root / "outside.md").write_text("outside", encoding="utf-8")
            self.validator.validate_local_links(skill / "SKILL.md", "[outside](../outside.md)", skill)
        self.assertTrue(any("outside package" in error for error in self.validator.errors))

    def test_symlink_outside_repository_is_not_read(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            outside = Path(directory) / "outside.md"
            outside.write_bytes(b'\xff')
            link = root / "link.md"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable on this platform")
            with patch.object(validate, "ROOT", root):
                self.validator.validate_repository_text()
        self.assertTrue(any("outside repository" in error for error in self.validator.errors))
        self.assertFalse(any("cannot read" in error for error in self.validator.errors))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX named pipes unavailable")
    def test_named_pipe_is_not_opened_as_repository_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            path = Path(directory) / "working-note.md"
            os.mkfifo(path)
            self.validator.validate_repository_text()
            self.assertEqual(self.validator.errors, [])
            self.assertIsNone(self.validator.read_text(path))
            self.assertTrue(any("not a regular file" in error for error in self.validator.errors))

    def test_generated_directories_are_not_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch.object(validate, "ROOT", Path(directory)):
            root = Path(directory)
            for name in validate.IGNORED_DIRECTORIES:
                generated = root / name
                generated.mkdir()
                (generated / "bad.py").write_bytes(b'\xff')
            self.validator.validate_repository_text()
        self.assertEqual(self.validator.errors, [])

    def test_unreadable_file_is_reported(self) -> None:
        with patch.object(Path, "read_text", side_effect=PermissionError("denied")):
            self.assertIsNone(self.validator.read_text(validate.SKILL_MD))
        self.assertTrue(any("cannot read" in error for error in self.validator.errors))

    def test_schema_fields_reject_arbitrary_json_values_without_crashing(self) -> None:
        values = (None, True, False, 1, 1.5, "", " ", [], {}, [None], {"unexpected": []})
        for original, check in ((self.manifest, self.check_manifest), (self.evals, self.check_evals)):
            for key in original:
                for value in values:
                    with self.subTest(key=key, value=value):
                        if type(value) is type(original[key]) and value == original[key]:
                            continue
                        data = copy.deepcopy(original)
                        data[key] = value
                        self.assertTrue(check(data))


if __name__ == "__main__":
    unittest.main()
