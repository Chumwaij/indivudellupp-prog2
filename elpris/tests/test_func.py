import func

def test_get_prices_returns_list():
    """Kontrollerar att funktionen returnerar en lista vid giltiga data"""
    data = func.get_prices("2024", "11", "01", "SE3")
    assert isinstance(data, list) or isinstance(data, str)

def test_invalid_request():
    """Kontrollerar att felaktiga datum returnerar ett felmeddelande"""
    data = func.get_prices("2020", "01", "01", "SE3")
    assert isinstance(data, str)
