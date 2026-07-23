# Security Policy

## Responsible use

`saas-audit` is intended only for systems, repositories, data and infrastructure the operator is authorized to assess. The skill prohibits destructive exploitation, denial-of-service, uncontrolled load, persistence, credential stuffing, production modification without explicit approval and data exfiltration.

## Reporting a vulnerability in this repository

Use GitHub's private vulnerability reporting or Security Advisories for `srksourabh/saas-audit` when available. Do not publish exploit details, live credentials, tokens, personal data or confidential tenant information in a public issue.

A useful report contains:

- affected file, script, installer or documented workflow;
- repository version or commit;
- safe reproduction steps;
- expected and actual behavior;
- impact and likely attack conditions;
- redacted evidence;
- suggested remediation where known.

## Supported version

Security fixes are applied to the latest version on the `main` branch. Users should reinstall or update their local skill copy after a security release.

## Secret handling

Never commit application credentials, API keys, session cookies, database URLs, private keys or real customer data. Use environment variables, dedicated test accounts and ignored local files. Redact all evidence and rotate any credential that may have been exposed.

## Safe testing boundary

The minimum proof required should be used to confirm a vulnerability. Stop a test when availability, integrity, privacy, customer data or unexpected cost is at risk. Mark unexecuted work as `BLOCKED` or `NOT_TESTED`; never infer a pass.

## Disclosure expectations

Allow reasonable time for investigation and remediation before public disclosure. Reports involving a third-party target should be sent to that target's authorized security channel, not to this repository, unless the defect is in the skill itself.

## No certification claim

Use of this skill does not constitute a formal penetration test, legal compliance assessment or security certification. Independent professional assurance may still be required.
