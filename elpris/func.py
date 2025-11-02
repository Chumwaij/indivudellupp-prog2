import requests

def get_prices(year, month, day, price_class):
    """tar fram elpriser genom apin och skriver ut lista som har pris och tid"""
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    # tar fram data från API
    response = requests.get(url)

    if response.status_code != 200:
        return "Kunde inte hämta data. Kontrollera datum och prisklass."

    # läser JSON-data
    try:
        data = response.json()
    except ValueError:
        return "Fel vid tolkning av data."

    prices = []
    # loopar igenom timmarna och tar fram tid och pris
    for item in data:
        time = item.get("time_start", "")[11:16]  # hh:mm-format
        price = round(item.get("SEK_per_kWh", 0), 3)
        prices.append((time, price))

    return prices
