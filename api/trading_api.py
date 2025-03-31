import requests
from ib_insync import IB, Stock

class TradingAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.crypto.com/v2/"

    def get_market_data(self):
        response = requests.get(f"{self.base_url}market", headers={"Authorization": f"Bearer {self.api_key}"})
        return response.json()

    def get_news_data(self):
        return [{"title": "Bitcoin hits $30k", "source": "Reuters"}]

    def place_order(self, decision):
        print(f"Placing order: {decision}")

class InteractiveBrokersAPI:
    def __init__(self, host='127.0.0.1', port=7497, client_id=1):
        self.ib = IB()
        self.ib.connect(host, port, clientId=client_id)

    def get_market_data(self, symbol):
        """
        Fetch market data for a given stock symbol.
        """
        stock = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(stock)
        ticker = self.ib.reqMktData(stock)
        self.ib.sleep(2)  # Allow time for data to populate
        return {
            "symbol": symbol,
            "last_price": ticker.last,
            "bid": ticker.bid,
            "ask": ticker.ask
        }

    def place_order(self, symbol, action, quantity):
        """
        Place an order for a given stock symbol.
        """
        stock = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(stock)
        order = self.ib.marketOrder(action, quantity)
        trade = self.ib.placeOrder(stock, order)
        return trade
