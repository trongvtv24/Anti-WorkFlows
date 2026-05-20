#!/usr/bin/env python3
"""Audit workflow-skill contracts and skill internal logic.

Generates:
- reports/workflow_skill_alignment_audit.md
- reports/workflow_skill_logic_audit.md

Use --strict to fail when any gap is found.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Gap:
    scope: str
    path: str
    message: str


HARD_CODED_PATH_PATTERNS = (
    re.compile(r"%USERPROFILE%", re.IGNORECASE),
    re.compile(r"\$env:USERPROFILE", re.IGNORECASE),
    re.compile(r"~/.gemini", re.IGNORECASE),
    re.compile(r"~/.antigravity", re.IGNORECASE),
    re.compile(r"\bz:\\", re.IGNORECASE),
)

TOOL_DEPENDENCY_MARKERS = (
    "search_web",
    "browser_subagent",
)

FALLBACK_MARKERS = (
    "fallback",
    "manual",
    "if unavailable",
    "if missing",
    "không có",
    "khong co",
    "manual-evidence",
)


def extract_frontmatter_and_body(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5 :]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception:
        fm = {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, body


def contains_any(text: str, markers: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in markers)


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run(root: Path, strict: bool) -> int:
    manifest_path = root / "awf_manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    workflows = manifest.get("workflows", [])
    skills = manifest.get("skills", [])

    workflow_by_command: dict[str, dict[str, Any]] = {}
    for wf in workflows:
        if isinstance(wf, dict) and isinstance(wf.get("command"), str):
            workflow_by_command[wf["command"]] = wf

    skill_by_name: dict[str, dict[str, Any]] = {}
    for skill in skills:
        if isinstance(skill, dict) and isinstance(skill.get("name"), str):
            skill_by_name[skill["name"]] = skill

    workflow_commands = set(workflow_by_command.keys())

    workflow_gaps: list[Gap] = []
    skill_gaps: list[Gap] = []
    alignment_rows: list[dict[str, Any]] = []

    # Workflow <-> skill contract checks
    for command, wf in sorted(workflow_by_command.items()):
        wf_path = root / wf["path"]
        wf_fm, wf_body = extract_frontmatter_and_body(wf_path)
        body_lower = wf_body.lower()

        required = list(wf.get("required_skills") or [])
        conditional = list(wf.get("conditional_skills") or [])
        declared = required + conditional

        related_issues: list[str] = []
        for skill_name in declared:
            skill = skill_by_name.get(skill_name)
            if not skill:
                related_issues.append(f"{skill_name}: missing in manifest skills")
                continue
            related_workflows = list(skill.get("related_workflows") or [])
            if "all" not in related_workflows and command not in related_workflows:
                related_issues.append(f"{skill_name}: related_workflows missing {command}")

        if related_issues:
            workflow_gaps.append(
                Gap(
                    scope=command,
                    path=wf["path"],
                    message="; ".join(related_issues),
                )
            )

        hooks = wf_fm.get("skill_hooks") if isinstance(wf_fm, dict) else {}
        hooks_req = list((hooks or {}).get("required") or [])
        hooks_cond = list((hooks or {}).get("conditional") or [])
        meta_issues: list[str] = []
        if hooks_req != required:
            meta_issues.append(f"required mismatch file={hooks_req} manifest={required}")
        if hooks_cond != conditional:
            meta_issues.append(f"conditional mismatch file={hooks_cond} manifest={conditional}")
        if meta_issues:
            workflow_gaps.append(
                Gap(
                    scope=command,
                    path=wf["path"],
                    message="; ".join(meta_issues),
                )
            )

        missing_mentions = [skill_name for skill_name in declared if skill_name.lower() not in body_lower]
        if missing_mentions:
            workflow_gaps.append(
                Gap(
                    scope=command,
                    path=wf["path"],
                    message=f"declared skills not mentioned in body: {', '.join(missing_mentions)}",
                )
            )

        if "skill activation contract" not in body_lower:
            workflow_gaps.append(
                Gap(
                    scope=command,
                    path=wf["path"],
                    message="missing 'Skill Activation Contract' section",
                )
            )

        hardcoded_hits = [pat.pattern for pat in HARD_CODED_PATH_PATTERNS if pat.search(wf_body)]
        if hardcoded_hits:
            workflow_gaps.append(
                Gap(
                    scope=command,
                    path=wf["path"],
                    message=f"hardcoded path patterns: {', '.join(hardcoded_hits)}",
                )
            )

        alignment_rows.append(
            {
                "workflow": command,
                "required": required,
                "conditional": conditional,
                "related": "OK" if not related_issues else "; ".join(related_issues),
                "metadata": "OK" if not meta_issues else "; ".join(meta_issues),
            }
        )

    # Skill internal logic checks
    for skill_name, skill in sorted(skill_by_name.items()):
        skill_path = root / skill["path"]
        fm, body = extract_frontmatter_and_body(skill_path)
        body_lower = body.lower()

        related_workflows = list(skill.get("related_workflows") or [])
        for command in related_workflows:
            if command != "all" and command not in workflow_commands:
                skill_gaps.append(
                    Gap(
                        scope=skill_name,
                        path=skill["path"],
                        message=f"related_workflows references unknown workflow: {command}",
                    )
                )

        fm_related = list((fm.get("related_workflows") or []) if isinstance(fm, dict) else [])
        if fm_related and fm_related != related_workflows:
            skill_gaps.append(
                Gap(
                    scope=skill_name,
                    path=skill["path"],
                    message=f"frontmatter related_workflows mismatch file={fm_related} manifest={related_workflows}",
                )
            )

        has_tool_dependency = contains_any(body, TOOL_DEPENDENCY_MARKERS)
        if has_tool_dependency and not contains_any(body, FALLBACK_MARKERS):
            skill_gaps.append(
                Gap(
                    scope=skill_name,
                    path=skill["path"],
                    message="mentions external tools but has no explicit fallback/manual mode guidance",
                )
            )

        risk_level = str(skill.get("risk_level", "")).lower()
        requires_confirmation = bool(skill.get("requires_confirmation"))
        if risk_level in {"high", "critical"} and not requires_confirmation:
            skill_gaps.append(
                Gap(
                    scope=skill_name,
                    path=skill["path"],
                    message="high/critical risk skill should require confirmation",
                )
            )

    timestamp = datetime.now().isoformat(timespec="seconds")

    alignment_lines = [
        "# Workflow-Skill Alignment Audit",
        "",
        f"Generated: {timestamp}",
        "",
        "| Workflow | Required Skills | Conditional Skills | Related-Workflow Mismatch | Metadata Mismatch |",
        "|---|---|---|---|---|",
    ]
    for row in alignment_rows:
        alignment_lines.append(
            "| {wf} | {req} | {cond} | {rel} | {meta} |".format(
                wf=row["workflow"],
                req=", ".join(row["required"]) if row["required"] else "-",
                cond=", ".join(row["conditional"]) if row["conditional"] else "-",
                rel=row["related"],
                meta=row["metadata"],
            )
        )
    write_text(root / "reports/workflow_skill_alignment_audit.md", "\n".join(alignment_lines) + "\n")

    workflow_gap_count = len(workflow_gaps)
    skill_gap_count = len(skill_gaps)
    total_gaps = workflow_gap_count + skill_gap_count

    logic_lines = [
        "# Workflow-Skill Logic Audit",
        "",
        f"Generated: {timestamp}",
        "",
        "## Summary",
        "",
        f"- Workflows checked: **{len(workflow_by_command)}**",
        f"- Skills checked: **{len(skill_by_name)}**",
        f"- Workflow contract gaps: **{workflow_gap_count}**",
        f"- Skill internal logic gaps: **{skill_gap_count}**",
        f"- Total gaps: **{total_gaps}**",
        "",
        "## Workflow Gaps",
        "",
    ]

    if workflow_gaps:
        for gap in workflow_gaps:
            logic_lines.append(f"- `{gap.scope}` · `{gap.path}`: {gap.message}")
    else:
        logic_lines.append("- None")

    logic_lines.extend(["", "## Skill Gaps", ""])
    if skill_gaps:
        for gap in skill_gaps:
            logic_lines.append(f"- `{gap.scope}` · `{gap.path}`: {gap.message}")
    else:
        logic_lines.append("- None")

    write_text(root / "reports/workflow_skill_logic_audit.md", "\n".join(logic_lines) + "\n")

    print(f"Generated: {rel(root, root / 'reports/workflow_skill_alignment_audit.md')}")
    print(f"Generated: {rel(root, root / 'reports/workflow_skill_logic_audit.md')}")
    print(f"Workflow gaps: {workflow_gap_count}")
    print(f"Skill gaps: {skill_gap_count}")
    print(f"Total gaps: {total_gaps}")

    if strict and total_gaps > 0:
        return 1
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit workflow-skill logic contracts.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (default: parent of tools/).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 when any logic gap is detected.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run(args.root.resolve(), strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
