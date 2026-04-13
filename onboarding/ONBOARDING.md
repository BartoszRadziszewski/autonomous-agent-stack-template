# Kwestionariusz Inicjalizacji (Q0-Q7)

Q1: Jaki jest cel biznesowy agenta?
Q2: Kto jest końcowym odbiorcą (Human-in-the-loop)?
Q3: Jakie bazy danych ma przeszukiwać?
...
Q7: Jakie są limity budżetowe (Token Cap)?


---
Przykład
# ONBOARDING.md — Stack Configuration Interview
# Run before every new stack build. Produces: stack_identity_card.yaml
# Claude: conduct this interview conversationally, one question at a time.

---

## Q0 — ROLE IDENTIFICATION (always first, not counted in 7)

Ask: "Are you primarily a developer/engineer, or a domain expert
      (business, operations, education, etc.)?"

- Developer   → use technical terms, skip analogies
- Domain user → plain language throughout
  Replace: "workflow anchor" → "describe one task step by step"
  Replace: "output format contract" → "what should the result look like?"
  Replace: "cost envelope" → "roughly how much per month on AI API costs?"

Record: respondent_role: developer | domain_user

---

## Q1 — PURPOSE

Ask (developer):   "What is this stack for? What problem does it solve?"
Ask (domain user): "What job should this AI system do for you?"

Score:
  Single, well-defined task                                → +0
  Multiple related tasks                                   → +1
  Complex orchestration across many task types             → +2

Record: stack_purpose

---

## Q2 — OUTCOMES

Ask: "What should the system produce? List all output types."

Score:
  1 output type                                            → +0
  2–3 output types                                         → +1
  4+ types OR real-time alerts + async artefacts           → +2

Record: stack_outcomes (list)

---

## Q3 — INTEGRATION CONTEXT

Ask: "Are you extending an existing system, or starting from scratch?"
If extending: "Which system? What language/framework? What data formats?"

Score:
  Greenfield                                               → +0
  Extending 1 known system with documented API             → +1
  Extending 2+ systems, or legacy integration required     → +2

Record: integration_context, existing_systems (list)

---

## Q4 — WORKFLOW ANCHOR

Ask: "Describe ONE complete task: what triggers it, what happens
      step by step, and what the final output looks like."

Analyse the described flow:
  Linear, single step                                      → +0
  Linear, multi-step                                       → +1
  Branching or parallel paths                              → +2

Record: workflow_anchor (plain text), workflow_parallel: true|false

---

## Q5 — OUTPUT FORMAT CONTRACT

Ask: "For each output you named — exact format, who receives it, where does it go?"

Score:
  Same format, same destination for all                    → +0
  Mixed formats, one destination                           → +1
  Mixed formats, multiple destinations                     → +2

Record: output_formats (list: type, format, recipient, destination)

---

## Q6 — COST ENVELOPE

Ask: "Monthly API budget — or 'unconstrained'?
      If there's a budget — what happens when it's reached:
      pause, downgrade model, or queue work?"

⚠️  IMPORTANT: Multi-agent stacks use ~15× more tokens than single-agent.
    If budget is declared: flag this multiplier explicitly before recommending
    multi-agent architecture.

Score:
  Unconstrained OR > $500/month                            → +0
  $50–500/month with declared degradation policy           → +1
  < $50/month OR no degradation policy declared            → -1

Record: cost_envelope, degradation_policy

---

## Q7 — ENVIRONMENT

Ask: "Where will this run — laptop, server, cloud, or hybrid?"

Score:
  Single Linux machine, full tooling                       → +0
  Hybrid (local + cloud)                                   → +1
  macOS / WSL2 (limited kernel isolation)                  → +0
  Constrained environment (shared server, no root)         → -1

Record: environment, linux_isolation_available: true|false

---

## COMPLEXITY SCORE → ARCHITECTURE

Sum scores from Q1–Q7.

```
SCORE   ARCHITECTURE                LOAD THESE FILES
──────────────────────────────────────────────────────────────────────
0–2     SINGLE AGENT                CLAUDE.md + relevant skill(s)
        One agent, tool use only.
        Always start here.

3–5     SINGLE AGENT + VERIFIER     + agent_worker.md
        Worker + Verifier pair.       + agent_verifier.md (in worker file)
        Add observability first.      + skill_verification.md
                                      + skill_observability.md

6–8     MINIMAL MULTI-AGENT         + agent_orchestrator.md
        Orchestrator + 2–3 Workers.   + skill_observability.md (FIRST)
        No Supervisor yet.            + rules_governance.md

9–11    FULL MULTI-AGENT             All agent files
        Orchestrator + Teams          All skill files
        + Supervisor.                 rules_governance.md
        Observability mandatory.      Pre-launch checklist required.

≥12     SCOPE REVIEW                 Ask: can 80% of value come
        Complexity too high.          from a score-6 architecture?
```

### Hard override rules (apply before score)

FORCE SINGLE AGENT if:
  - Prototype or proof of concept
  - Budget < $50/month without degradation policy
  - No measured failure rates yet from a simpler version
  - No one on team has operated a multi-agent system before

FORCE HUMAN REVIEW before multi-agent if:
  - Outputs affect regulated data (financial, medical, legal)
  - System will run unattended > 24h
  - No monitoring / alerting configured

---

## OUTPUT: STACK IDENTITY CARD

Write to: stack/config/stack_identity_card.yaml

```yaml
# Generated: {ISO_TIMESTAMP}
# Onboarding version: 1.0

respondent_role: developer | domain_user
stack_purpose: ""
stack_outcomes: []
integration_context: greenfield | extend
existing_systems: []
workflow_anchor: ""
workflow_parallel: false
output_formats: []
cost_envelope: "$X/month | unconstrained"
degradation_policy: halt | downgrade_model | queue_work
environment: local | cloud | hybrid
linux_isolation_available: true | false

complexity_score: 0
recommended_architecture: single | single_plus_verifier | minimal_multi | full_multi
architecture_rationale: ""

constraints: []
```

This file is the single source of truth for all architectural decisions.
Do not recreate it — reference it in every subsequent session.