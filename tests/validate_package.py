from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "README.md", "agents/roster.md",
    "protocols/delegation-protocol.md", "protocols/communication-protocol.md",
    "standards/definition-of-done.md", "standards/approval-and-safety.md",
    "schemas/task.schema.json", "templates/task-report.md",
    "templates/phase-report.md", "templates/decision-record.md",
    "workflows/phase1-activation.md", "tests/acceptance-tests.md"
]
errors = []
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

skill_path = ROOT / "SKILL.md"
if skill_path.exists():
    content = skill_path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append("SKILL.md is missing YAML frontmatter")
    else:
        parts = content.split("---", 2)
        frontmatter = parts[1] if len(parts) > 1 else ""
        for key in ("name:", "version:", "description:"):
            if key not in frontmatter:
                errors.append(f"SKILL.md frontmatter missing {key}")
    for heading in ("## Mission and scope", "## Workforce", "## Core operating loop",
                    "## Decision rights", "## Evidence and status integrity",
                    "## Reporting", "## Startup behavior"):
        if heading not in content:
            errors.append(f"SKILL.md missing section: {heading}")

schema_path = ROOT / "schemas/task.schema.json"
if schema_path.exists():
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        if schema.get("type") != "object":
            errors.append("Task schema root must be an object")
        for key in ("task_id", "product", "title", "objective", "assigned_role",
                    "status", "priority", "acceptance_criteria", "deliverables",
                    "verification_method"):
            if key not in schema.get("required", []):
                errors.append(f"Task schema missing required field: {key}")
    except Exception as exc:
        errors.append(f"Invalid JSON schema file: {exc}")

roster_path = ROOT / "agents/roster.md"
if roster_path.exists():
    roster = roster_path.read_text(encoding="utf-8")
    ids = re.findall(r"\|\s*(\d{2})\s*\|", roster)
    if len(ids) != 24 or len(set(ids)) != 24:
        errors.append(f"Expected 24 unique agent IDs, found {len(ids)}")

if errors:
    print("VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION: PASS")
print(f"Required files checked: {len(required)}")
print("Skill frontmatter and required sections: PASS")
print("Task schema JSON and required fields: PASS")
print("Agent roster: 24 unique roles")
