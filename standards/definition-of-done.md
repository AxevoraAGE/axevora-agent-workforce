# Definition of Done

## Task-level completion
A task may be marked `COMPLETED` only when:
- The requested work is implemented or the requested research deliverable is finished.
- All acceptance criteria are checked individually.
- Evidence is available and traceable.
- Relevant error and edge cases are tested where applicable.
- Regression risk is evaluated.
- Known limitations and dependencies are documented.
- Required review and owner approvals are recorded.

## Status distinctions
- `IMPLEMENTED`: work appears in the code or artifact; behavior may not yet be verified.
- `TESTED_AND_VERIFIED`: relevant tests ran and passed with evidence.
- `PARTIALLY_IMPLEMENTED`: some requirements are met; others remain.
- `NOT_IMPLEMENTED`: no implementation exists.
- `BLOCKED`: progress depends on unavailable input, access, approval, or service.
- `REQUIRES_PAID_SERVICE`: capability depends on a paid external service or integration.

## Evidence examples
Acceptable evidence may include:
- test command and actual output;
- reproducible manual test steps and observed result;
- commit hash and reviewed diff;
- screenshot or recording of the running application, when relevant;
- benchmark output with device/environment details;
- source links for research claims.

Not sufficient by itself:
- generated code without execution;
- an agent saying "done";
- a plan or mockup presented as a working feature;
- a test plan that was not executed;
- a passing build when runtime behavior was not tested.

## Phase completion
A phase closes only when all phase deliverables are present, acceptance tests have results, unresolved blockers are listed, and the owner approves phase closure.
