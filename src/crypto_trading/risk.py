"""Risk management engine (paper-trading only)."""
from typing import Dict, Any

MAX_RISK_PER_TRADE = {
    "majors": 0.02,
    "large_alts": 0.015,
    "defi": 0.01,
    "stables": 0.005,
    "high_vol": 0.005,
}

def check_risk(asset_class: str, proposed_size_pct: float, portfolio_vol: float = 0.0) -> bool:
    """Return True if the proposed position is within limits."""
    limit = MAX_RISK_PER_TRADE.get(asset_class, 0.005)
    if proposed_size_pct > limit:
        return False
    # Simple portfolio vol circuit breaker
    if portfolio_vol > 0.15:  # 15% realized
        return False
    return True

def position_size(equity: float, risk_pct: float, stop_distance: float) -> float:
    """Volatility-aware size (simplified)."""
    if stop_distance <= 0 or equity <= 0:
        return 0.0
    raw = (equity * risk_pct) / stop_distance
    return max(0.0, raw)
