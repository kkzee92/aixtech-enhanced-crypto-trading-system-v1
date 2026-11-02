"""Enhanced asset-class specific trading strategies (research/paper only)."""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import math

class BaseStrategy(ABC):
    """Abstract base for all strategies."""
    name: str = "base"

    @abstractmethod
    def generate_signal(self, data: Dict[str, Any]) -> str:
        """Return 'BUY', 'SELL', or 'HOLD'. Must be pure and side-effect free."""
        raise NotImplementedError

    def _safe_get(self, data: Dict[str, Any], key: str, default: float = 0.0) -> float:
        try:
            val = float(data.get(key, default))
            return val if math.isfinite(val) else default
        except (TypeError, ValueError):
            return default

class MajorsStrategy(BaseStrategy):
    """Multi-factor strategy for BTC/ETH majors."""
    name = "majors"

    def generate_signal(self, data: Dict[str, Any]) -> str:
        price = self._safe_get(data, "price")
        ema50 = self._safe_get(data, "ema_50", price)
        ema200 = self._safe_get(data, "ema_200", price)
        volume_ratio = self._safe_get(data, "volume_ratio", 1.0)
        funding = self._safe_get(data, "funding_rate", 0.0)

        # Trend filter
        if ema50 > ema200 and price > ema50 and volume_ratio > 1.5 and funding < 0.0005:
            return "BUY"
        if ema50 < ema200 and price < ema50 and volume_ratio > 1.5 and funding > -0.0005:
            return "SELL"
        # Mean reversion overlay (simplified)
        bb_upper = self._safe_get(data, "bb_upper", price * 1.02)
        bb_lower = self._safe_get(data, "bb_lower", price * 0.98)
        if price >= bb_upper:
            return "SELL"
        if price <= bb_lower:
            return "BUY"
        return "HOLD"

class LargeAltsStrategy(BaseStrategy):
    """Momentum + relative strength for large alts."""
    name = "large_alts"

    def generate_signal(self, data: Dict[str, Any]) -> str:
        price = self._safe_get(data, "price")
        btc_ratio_mom = self._safe_get(data, "btc_ratio_momentum", 0.0)
        volume_ratio = self._safe_get(data, "volume_ratio", 1.0)
        if btc_ratio_mom > 0.02 and volume_ratio > 1.8:
            return "BUY"
        if btc_ratio_mom < -0.02 and volume_ratio > 1.5:
            return "SELL"
        return "HOLD"

class DeFiStrategy(BaseStrategy):
    """Price + protocol health proxies."""
    name = "defi"

    def generate_signal(self, data: Dict[str, Any]) -> str:
        price_change = self._safe_get(data, "price_change_pct", 0.0)
        tvl_change = self._safe_get(data, "tvl_change_pct", 0.0)
        if price_change > 0.01 and tvl_change > 0.005:
            return "BUY"
        if price_change < -0.03 or tvl_change < -0.02:
            return "SELL"
        return "HOLD"

class StableStrategy(BaseStrategy):
    """Peg and premium monitoring."""
    name = "stables"

    def generate_signal(self, data: Dict[str, Any]) -> str:
        deviation = abs(self._safe_get(data, "peg_deviation_bps", 0.0))
        if deviation > 50:
            return "ALERT"  # special non-trade signal
        return "HOLD"

class HighVolStrategy(BaseStrategy):
    """Strict risk controls for speculative assets."""
    name = "high_vol"

    def generate_signal(self, data: Dict[str, Any]) -> str:
        # Always return HOLD unless very strong structured signal; size is handled in risk layer
        volume_ratio = self._safe_get(data, "volume_ratio", 1.0)
        price_change = self._safe_get(data, "price_change_pct", 0.0)
        if volume_ratio > 3.0 and abs(price_change) > 0.05:
            return "HOLD"  # anomaly - skip
        return "HOLD"

# Registry
STRATEGIES: Dict[str, BaseStrategy] = {
    "majors": MajorsStrategy(),
    "large_alts": LargeAltsStrategy(),
    "defi": DeFiStrategy(),
    "stables": StableStrategy(),
    "high_vol": HighVolStrategy(),
}

def get_strategy(asset_class: str) -> Optional[BaseStrategy]:
    return STRATEGIES.get(asset_class.lower())
