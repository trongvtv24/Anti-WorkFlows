import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from textwrap import dedent

from tools.audit_workflow_skill_logic import run


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


class AuditWorkflowSkillLogicTests(unittest.TestCase):
    @staticmethod
    def _run_quiet(root: Path, strict: bool) -> int:
        buffer = StringIO()
        with redirect_stdout(buffer):
            return run(root, strict=strict)

    def test_run_passes_and_generates_reports_when_contracts_are_valid(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(
                root / "awf_manifest.yaml",
                """
                workflows:
                  - command: "/demo"
                    name: "demo"
                    path: "global_workflows/demo.md"
                    category: "quality"
                    priority: "high"
                    risk_level: "low"
                    triggers: ["/demo"]
                    next_workflows: ["/demo"]
                    required_gates: []
                    required_skills: ["demo-skill"]
                    conditional_skills: []
                skills:
                  - name: "demo-skill"
                    path: "skills/demo-skill/SKILL.md"
                    category: "quality"
                    activation: "conditional"
                    priority: "medium"
                    risk_level: "low"
                    related_workflows: ["/demo"]
                    allowed_side_effects: ["none"]
                    requires_confirmation: false
                """,
            )
            _write(
                root / "global_workflows/demo.md",
                """
                ---
                type: workflow
                name: "demo"
                command: "/demo"
                category: "quality"
                risk_level: "low"
                skill_hooks:
                  required: ["demo-skill"]
                  conditional: []
                ---
                # Demo workflow

                ## Skill Activation Contract (Workflow ↔ Skill)
                - `demo-skill` handles the action.
                """,
            )
            _write(
                root / "skills/demo-skill/SKILL.md",
                """
                ---
                type: skill
                name: "demo-skill"
                related_workflows:
                  - "/demo"
                ---
                # Demo skill
                Use this skill for demo checks.
                """,
            )

            code = self._run_quiet(root, strict=True)
            self.assertEqual(code, 0)
            self.assertTrue((root / "reports/workflow_skill_alignment_audit.md").exists())
            self.assertTrue((root / "reports/workflow_skill_logic_audit.md").exists())

            logic_report = (root / "reports/workflow_skill_logic_audit.md").read_text(encoding="utf-8")
            self.assertIn("Workflow contract gaps: **0**", logic_report)
            self.assertIn("Skill internal logic gaps: **0**", logic_report)

    def test_run_strict_fails_when_workflow_contract_is_missing(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(
                root / "awf_manifest.yaml",
                """
                workflows:
                  - command: "/demo"
                    name: "demo"
                    path: "global_workflows/demo.md"
                    category: "quality"
                    priority: "high"
                    risk_level: "low"
                    triggers: ["/demo"]
                    next_workflows: ["/demo"]
                    required_gates: []
                    required_skills: ["demo-skill"]
                    conditional_skills: []
                skills:
                  - name: "demo-skill"
                    path: "skills/demo-skill/SKILL.md"
                    category: "quality"
                    activation: "conditional"
                    priority: "medium"
                    risk_level: "low"
                    related_workflows: ["/demo"]
                    allowed_side_effects: ["none"]
                    requires_confirmation: false
                """,
            )
            _write(
                root / "global_workflows/demo.md",
                """
                ---
                type: workflow
                name: "demo"
                command: "/demo"
                category: "quality"
                risk_level: "low"
                skill_hooks:
                  required: ["demo-skill"]
                  conditional: []
                ---
                # Demo workflow
                This body mentions demo-skill but intentionally has no activation contract heading.
                """,
            )
            _write(
                root / "skills/demo-skill/SKILL.md",
                """
                ---
                type: skill
                name: "demo-skill"
                related_workflows:
                  - "/demo"
                ---
                # Demo skill
                """,
            )

            code = self._run_quiet(root, strict=True)
            self.assertEqual(code, 1)

            logic_report = (root / "reports/workflow_skill_logic_audit.md").read_text(encoding="utf-8")
            self.assertIn("missing 'Skill Activation Contract' section", logic_report)

    def test_run_strict_fails_when_tool_dependency_has_no_fallback(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(
                root / "awf_manifest.yaml",
                """
                workflows:
                  - command: "/demo"
                    name: "demo"
                    path: "global_workflows/demo.md"
                    category: "quality"
                    priority: "high"
                    risk_level: "low"
                    triggers: ["/demo"]
                    next_workflows: ["/demo"]
                    required_gates: []
                    required_skills: ["demo-skill"]
                    conditional_skills: []
                skills:
                  - name: "demo-skill"
                    path: "skills/demo-skill/SKILL.md"
                    category: "quality"
                    activation: "conditional"
                    priority: "medium"
                    risk_level: "low"
                    related_workflows: ["/demo"]
                    allowed_side_effects: ["none"]
                    requires_confirmation: false
                """,
            )
            _write(
                root / "global_workflows/demo.md",
                """
                ---
                type: workflow
                name: "demo"
                command: "/demo"
                category: "quality"
                risk_level: "low"
                skill_hooks:
                  required: ["demo-skill"]
                  conditional: []
                ---
                # Demo workflow
                ## Skill Activation Contract (Workflow ↔ Skill)
                - `demo-skill` handles the action.
                """,
            )
            _write(
                root / "skills/demo-skill/SKILL.md",
                """
                ---
                type: skill
                name: "demo-skill"
                related_workflows:
                  - "/demo"
                ---
                # Demo skill
                Uses search_web for research.
                """,
            )

            code = self._run_quiet(root, strict=True)
            self.assertEqual(code, 1)

            logic_report = (root / "reports/workflow_skill_logic_audit.md").read_text(encoding="utf-8")
            self.assertIn("mentions external tools but has no explicit fallback/manual mode guidance", logic_report)


if __name__ == "__main__":
    unittest.main()
