# Master SaaS and Codebase Audit Checklist

Use this catalogue to create the coverage ledger. Mark every item `PASS`, `FAIL`, `BLOCKED`, `NOT_TESTED` or `NOT_APPLICABLE`. Add stack- and product-specific tests discovered during inventory.

## 1. Scope and evidence

- [ ] Authorization, environment, exclusions and production restrictions recorded.
- [ ] Repository commit and deployed version recorded.
- [ ] Roles, tenants, critical workflows and data classes identified.
- [ ] Evidence directory, execution log and coverage ledger created.
- [ ] Credentials use an approved secret mechanism and are not committed.
- [ ] Test data uses `AUDIT_TEST_` and cleanup is tracked.

## 2. Discovery and architecture

- [ ] Public, authenticated, privileged and hidden routes inventoried.
- [ ] Forms, tables, search, reports, uploads, downloads, imports and exports inventoried.
- [ ] APIs, GraphQL, WebSockets, SSE, webhooks, jobs, queues and cron inventoried.
- [ ] Roles, permissions, tenants, service accounts and impersonation paths inventoried.
- [ ] Database, policies, functions, migrations, storage, cache and search inventoried.
- [ ] Dependencies, CI/CD, IaC, containers, cloud and integrations inventoried.
- [ ] AI prompts, tools, RAG, vector stores and knowledge sources inventoried.
- [ ] Source and runtime inventories reconciled.
- [ ] Orphaned, undocumented or unreachable surfaces recorded.
- [ ] Trust boundaries and critical assets documented.

## 3. Build and engineering quality

- [ ] Canonical install and build succeeds.
- [ ] Type checking succeeds.
- [ ] Lint and formatting checks succeed.
- [ ] Unit, integration, E2E, migration and smoke tests run where available.
- [ ] Test failures, skips and flakes are explained.
- [ ] Critical workflows have automated tests.
- [ ] Role and tenant controls have automated tests.
- [ ] Error handling is consistent and actionable.
- [ ] Dead code, duplicated logic and hidden coupling reviewed.
- [ ] Large or high-risk modules have clear boundaries and owners.
- [ ] Configuration is environment-specific and validated.
- [ ] Documentation matches actual commands and architecture.

## 4. Authentication and account lifecycle

- [ ] Valid and invalid login behavior tested.
- [ ] Disabled, locked and unverified accounts tested.
- [ ] Password policy and breached/common-password controls reviewed.
- [ ] Reset tokens expire, are single-use and invalidate appropriately.
- [ ] MFA enrollment, challenge, recovery and bypass resistance tested.
- [ ] Login throttling and abuse protection tested safely.
- [ ] Sessions rotate after authentication and privilege changes.
- [ ] Idle and absolute session timeouts tested.
- [ ] Logout revokes server-side access.
- [ ] Password, email, role and tenant changes affect sessions correctly.
- [ ] Cookie flags and browser storage reviewed.
- [ ] OAuth/OIDC state, nonce, callbacks and account linking reviewed where applicable.

## 5. RBAC and authorization

- [ ] Expected role-action matrix documented.
- [ ] View, list, search, create, update and delete tested per role.
- [ ] Approve, reject, assign and reassign tested per role.
- [ ] Upload, download, import and export tested per role.
- [ ] Configure, invite, archive, restore and impersonate tested per role.
- [ ] Sensitive fields and administrative data tested per role.
- [ ] Direct route access tested.
- [ ] API object-level authorization tested.
- [ ] API function-level authorization tested.
- [ ] Horizontal privilege escalation tested.
- [ ] Vertical privilege escalation tested.
- [ ] Mass assignment of role, tenant and ownership fields tested.
- [ ] Permission changes apply without stale access.
- [ ] Server-side denial exists independently of UI visibility.

## 6. Multi-tenant and white-label isolation

- [ ] Two tenants tested with modified identifiers.
- [ ] Lists, details, search and autocomplete scoped.
- [ ] Tenant names, domains, logos and branding isolated.
- [ ] Users, invitations and membership metadata isolated.
- [ ] Files, filenames, buckets, signed URLs and CDN paths isolated.
- [ ] Reports, exports and scheduled reports isolated.
- [ ] Notifications, email and templates isolated.
- [ ] Webhooks and integration payloads isolated.
- [ ] Cache keys and invalidation include tenant context.
- [ ] Logs, analytics, metrics and errors do not reveal other tenants.
- [ ] Jobs, queues, cron and retry state retain tenant context.
- [ ] Search indexes and analytics stores are scoped.
- [ ] RAG, embeddings, vector stores and memory are scoped.
- [ ] Support and impersonation actions are authorized and audited.

## 7. Functional correctness

- [ ] Critical happy paths pass.
- [ ] Required fields and validation tested server-side.
- [ ] Minimum, maximum, boundary and malformed values tested.
- [ ] Duplicate submissions and double clicks tested.
- [ ] Refresh, back, interruption and cancellation tested.
- [ ] Slow network, timeout and retry tested.
- [ ] Concurrent and stale updates tested.
- [ ] Transactions prevent partial writes.
- [ ] Drafts and recoverable user work are preserved where expected.
- [ ] Bulk actions report partial success and failure correctly.
- [ ] Import validation and rollback behavior tested.
- [ ] Export data matches visible, filtered and authorized data.
- [ ] Pagination, sorting, filters and totals are consistent.
- [ ] Notifications and downstream side effects occur exactly once.
- [ ] Deletion, archive and restore preserve integrity.

## 8. UI and UX

- [ ] Navigation and information architecture are understandable.
- [ ] Primary and secondary actions are clear and consistent.
- [ ] Labels and terminology are consistent.
- [ ] Loading, empty, error, success and permission states exist.
- [ ] Destructive actions are separated and proportionately confirmed.
- [ ] Errors explain what happened and how to recover.
- [ ] Unsaved changes and draft behavior are deliberate.
- [ ] Desktop, tablet and mobile layouts tested.
- [ ] Tables and complex controls remain usable responsively.
- [ ] Touch targets and spacing are adequate.
- [ ] First-time users can discover critical actions.
- [ ] Repeated patterns use consistent components.

## 9. Accessibility

- [ ] All critical workflows operate by keyboard.
- [ ] Focus order is logical and focus is visible.
- [ ] Dialogs move and restore focus correctly.
- [ ] Native semantics are used before ARIA.
- [ ] Page titles, headings and landmarks are meaningful.
- [ ] Inputs have programmatic labels and errors.
- [ ] Status and error updates are announced.
- [ ] Contrast and non-color indicators are sufficient.
- [ ] Zoom and reflow are usable.
- [ ] Icon buttons have accessible names.
- [ ] Menus, tabs, comboboxes and dialogs follow expected keyboard behavior.
- [ ] Data tables expose headers and relationships.
- [ ] Motion respects reduced-motion preferences where relevant.

## 10. Application security

- [ ] Inputs are validated at trust boundaries.
- [ ] SQL, document-query, command, template and expression injection reviewed.
- [ ] Reflected, stored and DOM XSS reviewed.
- [ ] CSRF protections cover state-changing browser requests.
- [ ] Open redirects and untrusted URL handling reviewed.
- [ ] SSRF indicators and outbound request controls reviewed.
- [ ] Path traversal and filename manipulation reviewed.
- [ ] Unsafe deserialization and parser behavior reviewed.
- [ ] Output is encoded by context.
- [ ] Security headers and TLS behavior reviewed.
- [ ] Debug endpoints, stack traces and source maps reviewed.
- [ ] Browser storage contains no unnecessary secrets or sensitive data.
- [ ] Business workflows resist bypass and duplicate execution.

## 11. File handling

- [ ] Upload authorization and tenant scope tested.
- [ ] Extension, content type and magic bytes validated.
- [ ] Size and resource limits enforced safely.
- [ ] Names and paths normalized.
- [ ] Uploaded content processed in isolation where expected.
- [ ] Malware scanning behavior reviewed where required.
- [ ] Download authorization and tenant scope tested.
- [ ] Signed URLs expire and cannot be broadened.
- [ ] Content-Disposition and content types are safe.
- [ ] Deleted or expired objects are no longer accessible.

## 12. API security and quality

- [ ] Authentication required consistently.
- [ ] Object and function authorization tested.
- [ ] Tenant scope enforced server-side.
- [ ] Schemas reject malformed and unknown fields.
- [ ] Mass assignment blocked.
- [ ] Responses do not expose unnecessary fields.
- [ ] Pagination and query complexity bounded.
- [ ] Rate limits and abuse controls tested safely.
- [ ] CORS is least permissive.
- [ ] Content types and methods validated.
- [ ] Idempotency and replay behavior tested.
- [ ] Errors are consistent and non-sensitive.
- [ ] Versioning and deprecation policy reviewed.
- [ ] Undocumented endpoints recorded.

## 13. Database and integrity

- [ ] Primary, foreign, unique and check constraints reviewed.
- [ ] Nullability and defaults are correct.
- [ ] Money, decimal precision and rounding tested.
- [ ] Time zones and date boundaries tested.
- [ ] Related writes use transactions.
- [ ] Retries do not duplicate records.
- [ ] Concurrent updates do not silently overwrite.
- [ ] Soft delete, restore and referential integrity tested.
- [ ] Tenant predicates and row-level security reviewed.
- [ ] Sensitive fields encrypted or protected appropriately.
- [ ] Slow queries, indexes and N+1 patterns reviewed.
- [ ] Orphan and inconsistent records can be detected and reconciled.

## 14. Migrations and release data safety

- [ ] Migration order and application compatibility reviewed.
- [ ] Locks and table rewrites assessed.
- [ ] Backfills are resumable and observable.
- [ ] Data validation occurs before and after migration.
- [ ] Rollback or forward-fix documented.
- [ ] Partial execution recovery tested.
- [ ] Production-like volume considered.
- [ ] Expand-contract used where safer.
- [ ] Irreversible operations require explicit approval and backup.

## 15. Storage, cache and search

- [ ] Public access and bucket policies reviewed.
- [ ] Object naming and signed URL expiry reviewed.
- [ ] Encryption and lifecycle rules reviewed.
- [ ] Tenant context included in cache/search keys.
- [ ] Stale authorization and invalidation tested.
- [ ] Cache poisoning and cross-tenant results tested safely.
- [ ] Search result authorization and indexing delay tested.
- [ ] Deletion propagates to caches, search and CDN as expected.

## 16. Jobs, queues, cron and webhooks

- [ ] Idempotency and deduplication implemented.
- [ ] Retry backoff and limits are bounded.
- [ ] Poison messages and dead-letter handling exist.
- [ ] Tenant and authorization context propagate safely.
- [ ] Ordering assumptions documented and tested.
- [ ] Cron overlap and duplicate scheduling handled.
- [ ] Webhook signatures and replay windows verified.
- [ ] Partial failure and compensation defined.
- [ ] Reconciliation and manual recovery available.
- [ ] Logs and metrics expose processing health.

## 17. Dependencies and supply chain

- [ ] Lockfiles committed and respected.
- [ ] Direct and transitive vulnerabilities reviewed by reachability and impact.
- [ ] Abandoned or unmaintained dependencies identified.
- [ ] Package provenance and install scripts reviewed.
- [ ] Licenses and distribution obligations reviewed.
- [ ] SBOM generation readiness reviewed.
- [ ] Secrets and private registry tokens protected.
- [ ] Dependency update ownership and cadence defined.

## 18. CI/CD and infrastructure

- [ ] Workflow permissions follow least privilege.
- [ ] Untrusted fork and pull-request behavior is safe.
- [ ] Required checks and branch protection exist.
- [ ] Environments and secrets are separated.
- [ ] Artifacts and deployments are traceable.
- [ ] Production deployment requires appropriate approval.
- [ ] Rollback and smoke tests are documented and tested.
- [ ] IaC is reviewed and version controlled.
- [ ] Public exposure and network boundaries reviewed.
- [ ] Cloud identities and service accounts use least privilege.
- [ ] Containers avoid root and unnecessary capabilities.
- [ ] Images are pinned and scanned.
- [ ] DNS, TLS, CDN and WAF configuration reviewed.
- [ ] Quotas, autoscaling and cost controls reviewed.

## 19. Reliability and observability

- [ ] Timeouts are explicit and proportionate.
- [ ] Retries cannot create storms or duplicates.
- [ ] Graceful degradation exists for dependencies.
- [ ] Correlation IDs connect user, API and job activity safely.
- [ ] Logs are structured and redact sensitive data.
- [ ] Metrics cover critical workflows and resources.
- [ ] Traces identify latency and dependency failures.
- [ ] Alerts are actionable and owned.
- [ ] Runbooks exist for critical alerts.
- [ ] Backup restore is tested.
- [ ] RTO and RPO are defined and credible.
- [ ] Disaster recovery responsibilities are documented.

## 20. Performance

- [ ] Critical pages and APIs measured.
- [ ] Slow queries and N+1 behavior reviewed.
- [ ] Bundles, images and fonts optimized.
- [ ] Duplicate network requests eliminated.
- [ ] Large results paginate or stream.
- [ ] Search, export and upload performance tested safely.
- [ ] Caching preserves security and freshness.
- [ ] Performance budgets and regression checks exist.
- [ ] No uncontrolled load testing performed.

## 21. Privacy and compliance readiness

- [ ] Data inventory and classification exist.
- [ ] Collection is minimized and purpose-aligned.
- [ ] Consent and preference behavior reviewed where applicable.
- [ ] Access, correction, export and deletion workflows tested.
- [ ] Retention is documented and enforced.
- [ ] Logs and analytics mask sensitive data.
- [ ] Browser storage is minimized.
- [ ] Third-party processors and data flows documented.
- [ ] Backup retention aligns with deletion commitments.
- [ ] Report avoids unsupported legal compliance claims.

## 22. AI and LLM features

- [ ] Direct and indirect prompt injection tested safely.
- [ ] Untrusted documents and retrieved content are treated as data, not instructions.
- [ ] Tool arguments validated.
- [ ] Tools use least privilege.
- [ ] Irreversible actions require confirmation.
- [ ] Model output rendered safely.
- [ ] RAG and vector stores enforce tenant isolation.
- [ ] Conversation memory and caches enforce tenant/user isolation.
- [ ] Sensitive prompts, responses and tool calls are protected in logs.
- [ ] Failure, refusal, timeout and fallback behavior tested.
- [ ] Human oversight exists for high-impact decisions.

## 23. Recommendations and retesting

- [ ] Every Critical/High finding has containment.
- [ ] Permanent fixes address root cause at the correct layer.
- [ ] Recommendations match the discovered stack.
- [ ] Owners, effort and target milestones assigned.
- [ ] Validation steps are exact and executable.
- [ ] Regression tests defined.
- [ ] Original reproduction retested.
- [ ] Adjacent roles, tenants and surfaces retested.
- [ ] Residual risk recorded.
- [ ] Findings JSON validates.

## 24. Final release gate

- [ ] No unresolved Critical or High blocker.
- [ ] Authentication, authorization and tenant isolation have evidence.
- [ ] Critical workflows tested.
- [ ] Build and required tests pass.
- [ ] Migrations and rollback are safe.
- [ ] Monitoring, alerting and incident ownership exist.
- [ ] Blocked and untested coverage is explicit.
- [ ] Conditional exceptions have owners, dates and controls.
- [ ] Final verdict matches findings and coverage.
- [ ] Human release owner remains accountable.
