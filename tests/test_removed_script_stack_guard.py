import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


FORBIDDEN_PATHS = (
    "global_workflows/script.md",
    "skills/squirrel-scriptwriter",
    "skills/timestamp-to-visual-prompt",
    "skills/squirrel-video-director",
    "skills/manim-video",
    "skills/remotion-video-creation",
)


FORBIDDEN_PATTERNS = (
    (r"(?<!<)/script\b", "workflow command /script"),
    (r"\bsquirrel-scriptwriter\b", "skill squirrel-scriptwriter"),
    (r"\btimestamp-to-visual-prompt\b", "skill timestamp-to-visual-prompt"),
    (r"\bsquirrel-video-director\b", "skill squirrel-video-director"),
    (r"\bmanim-video\b", "skill manim-video"),
    (r"\bremotion-video-creation\b", "skill remotion-video-creation"),
)


SCAN_GLOBS = (
    "awf_manifest.yaml",
    "README.md",
    "README.vi.md",
    ".github/workflows/*.yml",
    "global_workflows/**/*.md",
    "skills/**/*.md",
    "tools/**/*.py",
    "tests/**/*.py",
    "reports/**/*.md",
)


class RemovedScriptStackGuardTests(unittest.TestCase):
    def test_forbidden_paths_do_not_exist(self) -> None:
        existing = [path for path in FORBIDDEN_PATHS if (REPO_ROOT / path).exists()]
        self.assertEqual(
            existing,
            [],
            f"Forbidden workflow/skill paths must stay removed, found: {existing}",
        )

    def test_forbidden_tokens_do_not_reappear(self) -> None:
        compiled = [(re.compile(pattern, re.IGNORECASE), label) for pattern, label in FORBIDDEN_PATTERNS]
        findings: list[str] = []
        scanned_files: set[Path] = set()

        for pattern in SCAN_GLOBS:
            for path in REPO_ROOT.glob(pattern):
                if not path.is_file():
                    continue
                if path in scanned_files:
                    continue
                if path.name == "test_removed_script_stack_guard.py":
                    continue
                scanned_files.add(path)
                text = path.read_text(encoding="utf-8", errors="ignore")
                rel = path.relative_to(REPO_ROOT).as_posix()

                for regex, label in compiled:
                    if regex.search(text):
                        findings.append(f"{label} found in {rel}")

        self.assertEqual(findings, [], "Removed /script stack reappeared:\n" + "\n".join(findings))


if __name__ == "__main__":
    unittest.main()
