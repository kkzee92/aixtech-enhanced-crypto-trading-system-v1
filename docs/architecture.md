# Architecture Overview

Modular, paper-trading-only information system.

```mermaid
flowchart LR
    subgraph Data
        Public[Public Market APIs]
        Synthetic[Synthetic Fixtures]
    end
    subgraph Core
        Ingest[Validated Ingestion]
        Feat[Feature Engineering]
        Strat[Strategy Registry]
        Risk[Risk Engine]
        Out[Signals / Logs]
    end
    subgraph Security
        ZT[Zero-Trust Controls]
        Audit[Audit Logging]
        CI[CI Security Gates]
    end
    Public --> Ingest
    Synthetic --> Ingest
    Ingest --> Feat --> Strat --> Risk --> Out
    ZT -.-> Ingest
    ZT -.-> Strat
    Audit -.-> Out
    CI -.-> Core
```

## Key Modules
- `strategies.py`: Asset-class strategy implementations + registry
- `risk.py`: Position limits, volatility circuit breakers
- `cli.py`: Demo entrypoint
- CI workflow + AGENTS.md for safe agent collaboration

All paths are designed to remain offline-testable and free of live execution code.
