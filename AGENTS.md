# Agent Rules for AIxTech Enhanced Crypto Trading System

One source of truth for AI coding agents (Claude Code, Cursor, Copilot, Grok, etc.).

## Core Rules
1. **Paper-trading only.** Never implement live order placement or withdrawal logic. All execution paths must remain simulation / logging.
2. **No secrets.** Never hard-code API keys, private keys, seeds, or credentials. Use environment variables only. Fail closed if missing.
3. **Public data only.** Use only public market data endpoints. No private user data, no PII.
4. **Security first.** Prefer zero-trust patterns, input validation, rate-limit awareness, and audit logging.
5. **Testable acceptance.** Every change must include or update tests. Coverage target ≥ 80%.
6. **Disclosure.** Commit messages must include `AI-Assisted: yes` trailer when agent-generated.
7. **Human review.** Definition of Done = CI green + human approval (see harness/definition-of-done.md).
8. **No financial advice.** Code and docs must carry disclaimers. Strategies are research signals only.

## Forbidden
- Live trading clients with order/withdrawal scopes
- Storing or logging real user funds or keys
- Circumventing CI security gates
- Inventing performance numbers without synthetic fixture labels

## Preferred Patterns
- Modular strategy classes inheriting from BaseStrategy
- Injectable data fetchers for offline tests
- Explicit risk checks before any signal is emitted
- Structured logging (JSON) for auditability
