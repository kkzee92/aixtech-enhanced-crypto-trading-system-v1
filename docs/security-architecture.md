# Cyber and Data Security Architecture

## Design Principles
- **Zero Trust**: authenticate and authorize every request; assume breach.
- **Least Privilege**: minimal permissions; paper-trading scopes only.
- **Defense in Depth**: multiple overlapping controls.
- **Encryption**: TLS 1.3+ in transit; AES-256 (or equivalent) at rest for any local state.
- **Auditability**: structured logs, immutable audit trail where possible.
- **Data Minimization**: only public market data; no PII, no user funds data.

## Controls
| Layer | Control | Implementation Notes |
|-------|---------|----------------------|
| Secrets | Env vars + optional Vault/AWS Secrets Manager | Never commit; CI gitleaks gate |
| API | Key rotation, IP allow-list (where supported), request signing | Read-only public endpoints preferred |
| Ingestion | Schema validation, rate-limit handling, anomaly flags | Reject unexpected fields |
| Processing | Input sanitization, no eval/exec of external data | |
| Storage | Encrypted local files / DB; short retention | |
| Monitoring | Anomaly detection on signal volume, size, frequency | Alert on outliers |
| CI/CD | Secret scan, dependency audit, license allow-list, lint, coverage | See `.github/workflows/ci.yml` |
| Agent | AGENTS.md rules + PDPA-like guard on fixtures | No personal data in prompts |

## Threat Model (selected)
- API key compromise → mitigated by least privilege + rotation + monitoring
- Data poisoning of signals → validation + multi-source confirmation
- Insider / agent misuse → human review gate + audit logs
- Exchange outage / rate limits → graceful degradation, circuit breakers

## Runbooks
Documented in code comments and future `docs/runbooks/`. All changes require human review before merge.
