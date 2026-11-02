# Enhanced Trading Strategies by Asset Class

All strategies produce research signals only. They are designed for backtesting and paper simulation. Past performance of any proxy does not indicate future results.

## Majors (BTC, ETH)
**Multi-factor trend + regime:**
- 50/200 EMA crossover for primary trend
- Volume confirmation (> 1.5× 20-period average)
- Funding rate & open-interest change filters (avoid crowded longs)
- Mean-reversion overlay when ADX < 20 (Bollinger Band extremes)
- Position size scaled by realized volatility

## Large-Cap Alts (SOL, BNB, ADA, etc.)
- Relative strength vs BTC (price ratio momentum)
- Volume breakout above 2× average
- Correlation filter: reduce size when BTC correlation > 0.8
- Time-stop: exit if no follow-through within N bars

## DeFi Tokens (UNI, AAVE, LINK, etc.)
- Price action + protocol health proxies (TVL change, fee revenue trends where available)
- Volatility harvesting signals (range-bound grid-like entries)
- Liquidity risk flag: wider stops or skip if depth is thin

## Stablecoins
- Cross-exchange premium / discount detection
- Yield differential signals (lending rates vs alternatives)
- Peg stability monitoring (deviation > 50 bps triggers alert)

## High-Volatility / Speculative (memecoins, new listings)
- Maximum 0.5–1% of portfolio risk per idea
- Hard stop-loss at 5–8% and time-based exit (e.g., 4 hours or end of session)
- No averaging down
- Anomaly filter: skip if sudden volume spike without prior structure

## Common Enhancements
- Adaptive position sizing (volatility targeting)
- Portfolio-level correlation risk check
- Explicit regime detection (trend / range / high-vol)
- Offline backtest hooks with synthetic fixtures

All strategies implement the `BaseStrategy.generate_signal` interface and can be registered in the strategy map.
