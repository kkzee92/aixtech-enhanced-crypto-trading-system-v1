from crypto_trading.strategies import get_strategy, MajorsStrategy

def test_majors_buy():
    s = MajorsStrategy()
    data = {"price": 100, "ema_50": 95, "ema_200": 90, "volume_ratio": 2.0, "funding_rate": 0.0}
    assert s.generate_signal(data) == "BUY"

def test_majors_hold():
    s = get_strategy("majors")
    data = {"price": 100, "ema_50": 100, "ema_200": 100, "volume_ratio": 1.0}
    assert s.generate_signal(data) == "HOLD"

def test_unknown_class():
    assert get_strategy("unknown") is None
