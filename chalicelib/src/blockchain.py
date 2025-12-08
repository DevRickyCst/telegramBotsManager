import requests


class BockchainInterface:
    """Interface in order to interact with blockchain"""

    def __init__(self):
        self.coin_market_cap_url = "https://pro-api.coinmarketcap.com/"
        self.coin_market_cap_url_header = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "e33a36dd-4270-4cfe-85f2-968be4427153",
        }

    def getPrice(self, symbol: str = "BTC", device: str = "USDT"):
        print(f"Getting price for {symbol}/{device}")
        symbol = symbol.upper().replace(" ", "")
        url = (
            self.coin_market_cap_url
            + f"v2/cryptocurrency/quotes/latest?symbol={symbol},device"
        )

        response = requests.get(url, headers=self.coin_market_cap_url_header).json()

        price = response["data"][symbol][0]["quote"]["USD"]["price"]
        return str(round(price, 2)) + "$"
