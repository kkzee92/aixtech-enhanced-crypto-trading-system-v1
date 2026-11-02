"""Simple CLI for demo / paper signals."""
import argparse
from .strategies import get_strategy

def main():
    parser = argparse.ArgumentParser(description="Paper-trading signal demo")
    parser.add_argument("command", choices=["demo"], help="Command to run")
    args = parser.parse_args()

    if args.command == "demo":
        print("=== AIxTech Enhanced Crypto Trading System - Paper Demo ===")
        print("Disclaimer: Research/educational only. Not financial advice. No live orders.\n")
        sample = {
            "majors": {"price": 65000, "ema_50": 64000, "ema_200": 60000, "volume_ratio": 1.8, "funding_rate": 0.0001},
            "large_alts": {"price": 150, "btc_ratio_momentum": 0.03, "volume_ratio": 2.1},
            "defi": {"price_change_pct": 0.015, "tvl_change_pct": 0.008},
        }
        for cls, data in sample.items():
            strat = get_strategy(cls)
            if strat:
                sig = strat.generate_signal(data)
                print(f"{cls:12} -> {sig}")
        print("\nSee docs/trading-strategies.md and docs/security-architecture.md for details.")

if __name__ == "__main__":
    main()
