# Architecture and Workflow

## Design goal

`saas-audit` is structured for progressive disclosure: a compact `SKILL.md` controls execution, while specialized references are loaded only when the active audit phase needs them. This reduces context overhead and avoids repeating the same instructions.

## Skill architecture

```mermaid
flowchart TB
    U[User request and authorized scope] --> S[SKILL.md orchestration]
    S --> E[Execution playbook]
    S --> R[Security, RBAC and tenancy]
    S --> Q[Quality, UX and accessibility]
    S --> D[Data, API and infrastructure]
    S --> P[Evidence, recommendations and release gates]
    S --> M[Master audit checklist]

    E --> W[Audit workspace]
    R --> F[Evidence-backed findings]
    Q --> F
    D --> F
    M --> F

    F --> J[JSON schema validation]
    J --> X[Remediation and retest]
    X --> H[HTML and PDF rendering]
    H --> O[Release verdict and evidence pack]
```

## End-to-end audit sequence

```mermaid
sequenceDiagram
    actor User
    participant Agent
    participant Repo as Codebase
    participant App as Running SaaS
    participant Data as Data and Infrastructure
    participant Evidence as Evidence Store
    participant Report as Report and Verdict

    User->>Agent: Scope, authorization, URL, roles and constraints
    Agent->>Repo: Discover architecture, routes, dependencies and tests
    Agent->>App: Inventory pages, workflows and runtime states
    Agent->>Data: Inspect authorized database and infrastructure controls
    Agent->>Repo: Run build, type, lint, test and safe scans
    Agent->>App: Test browser, API, RBAC and tenant boundaries
    Agent->>Evidence: Store screenshots, logs, code references and commands
    Agent->>Report: Classify findings and calculate risk
    Agent->>Report: Generate prioritized recommendations
    Agent->>App: Retest fixes and adjacent trust boundaries
    Agent->>Report: Issue SHIP, CONDITIONAL SHIP or DO NOT SHIP
    Agent-->>User: Findings, quality gains, roadmap and artifact paths
```

## Efficiency model

```mermaid
flowchart LR
    I[One discovery inventory] --> C[Shared coverage ledger]
    C --> T1[Code tests]
    C --> T2[Runtime tests]
    C --> T3[Security tests]
    C --> T4[UX and accessibility tests]
    C --> T5[Data and operations tests]
    T1 --> E[Unified evidence]
    T2 --> E
    T3 --> E
    T4 --> E
    T5 --> E
    E --> F[One finding model]
    F --> R[One remediation roadmap]
    R --> G[One release gate]
```

The skill avoids duplicated effort by using one surface inventory, one evidence model, one severity system and one release decision. A route discovered during functional QA is reused for authorization, tenancy, accessibility, performance and regression coverage.

## Evidence model

```mermaid
flowchart LR
    T[Test execution] --> E1[Screenshot]
    T --> E2[Console or network log]
    T --> E3[API request and response]
    T --> E4[Code or configuration reference]
    T --> E5[Command output]
    T --> E6[Database or infrastructure observation]
    E1 --> F[Finding]
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F
    E6 --> F
    F --> S[Severity and risk]
    F --> R[Recommendation]
    F --> X[Retest]
    S --> G[Release gate]
    R --> G
    X --> G
```

## Trust boundaries

The audit treats each of these as an explicit boundary:

- anonymous visitor to authenticated application;
- user to user;
- lower role to privileged role;
- tenant to tenant;
- browser to API;
- API to database, storage, cache and queues;
- application to third-party services;
- CI/CD to production;
- human instruction to AI agent;
- model output to tool execution;
- untrusted documents to RAG and vector memory.

## Test and finding states

```mermaid
stateDiagram-v2
    [*] --> Planned
    Planned --> Pass: Executed and expected
    Planned --> Fail: Defect confirmed
    Planned --> Blocked: Missing access or tool
    Planned --> NotTested: Intentionally skipped
    Planned --> NotApplicable: Feature absent
    Fail --> Confirmed
    Fail --> Probable
    Fail --> Observation
    Fail --> FalsePositive
    Confirmed --> RetestPass: Fix verified
    Confirmed --> RetestFail: Fix ineffective
    RetestPass --> [*]
```

## Non-negotiable design principles

1. Evidence before claims.
2. Server-side enforcement before UI assumptions.
3. Tenant isolation across every shared subsystem.
4. Safe, non-destructive testing.
5. Explicit limitations and blocked coverage.
6. Critical and High findings block release by default.
7. Recommendations must include validation and regression tests.
8. Human release authorization remains mandatory.
