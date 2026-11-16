# AXEVORA Phase 1 — Master Orchestrator Skill

This package contains the first reusable skill for the AXEVORA Agent Workforce.

## Contents
- `SKILL.md` — core orchestration instructions.
- `agents/roster.md` — the 24-role workforce roster and boundaries.
- `protocols/delegation-protocol.md` — task handoff rules.
- `protocols/communication-protocol.md` — agent-to-agent message format.
- `standards/definition-of-done.md` — evidence-based completion gates.
- `standards/approval-and-safety.md` — approval boundaries and safety rules.
- `schemas/task.schema.json` — machine-readable task structure.
- `templates/` — task, phase, and decision report templates.
- `workflows/phase1-activation.md` — startup checklist.
- `tests/acceptance-tests.md` — manual acceptance test plan.
- `tests/validate_package.py` — local package structure validator.

## Important deployment note
This is a skill package, not a running multi-agent service. Actual delegation to separate autonomous agents requires a compatible runtime, tool access, and permissions. In a ChatGPT/Codex environment, install or reference the skill according to that environment's supported skill mechanism. Google AI Studio remains an implementation workflow and does not automatically execute this skill as a separate agent.

## Local validation
Run:
```bash
python tests/validate_package.py
```

The validator checks required files, YAML frontmatter, required sections, and JSON schema syntax. It does not prove runtime integration or real agent execution.
