import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.validate_awf import AwfValidator


class HarnessContractValidationTests(unittest.TestCase):
    def test_missing_harness_templates_are_reported(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            validator = AwfValidator(root)

            validator.validate_harness_contracts()

            messages = {issue.message for issue in validator.errors}
            self.assertIn("Missing harness artifact: harness/FEATURE_INTAKE.md", messages)
            self.assertIn("Missing harness artifact: harness/templates/story.md", messages)

    def test_story_template_requires_core_sections(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            story = root / "harness" / "templates" / "story.md"
            story.parent.mkdir(parents=True)
            story.write_text("# Story\n\n## Status\nplanned\n", encoding="utf-8")

            validator = AwfValidator(root)
            validator.validate_harness_template_sections(
                "harness/templates/story.md",
                ("## Product Contract", "## Acceptance Criteria", "## Validation", "## Evidence"),
            )

            messages = [issue.message for issue in validator.errors]
            self.assertIn("Missing required section: ## Product Contract", messages)
            self.assertIn("Missing required section: ## Evidence", messages)


if __name__ == "__main__":
    unittest.main()
