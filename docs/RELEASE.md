# Release checklist

Use this checklist for every Plugin release.

1. Recheck the current official OpenAI Skills and Plugins documentation for surface support and manifest changes.
2. Run `python3 scripts/validate.py`.
3. Run the current authoring environment's official Skill and Plugin validators.
4. Execute the behavioral cases in fresh conversations, including the negative implicit-trigger case.
5. Review permissions and confirm that no MCP, app, hook, or external data dependency was added unintentionally.
6. Update the manifest semantic version and `CHANGELOG.md`.
7. Confirm that README, migration, architecture, and evaluation claims match the package.
8. Confirm the repository contains no secrets, temporary artifacts, or untracked release files.
9. Resolve the license before external redistribution or contribution intake.
10. Build the submission archive from `plugins/cognitive-agent-skills` only and run the platform submission checks.

Do not treat a repository tag as proof that the public Plugin Directory accepted or published the package.
