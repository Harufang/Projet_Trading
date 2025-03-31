from api.trading_api import TradingAPI
from ai.sentiment_analysis import SentimentAnalyzer
from ai.decision_engine import DecisionEngine
from ai.backtesting import Backtester
from config.settings import API_KEYS

def main():
    # Initialisation des modules
    trading_api_crypto = TradingAPI(API_KEYS['crypto'])
    trading_api_stocks = TradingAPI(API_KEYS['stocks'])  # Added stock API initialization
    sentiment_analyzer = SentimentAnalyzer()
    decision_engine = DecisionEngine()
    backtester = Backtester()

    # Exemple de workflow pour crypto
    market_data_crypto = trading_api_crypto.get_market_data()
    news_data_crypto = trading_api_crypto.get_news_data()
    sentiment_scores_crypto = sentiment_analyzer.analyze(news_data_crypto)
    decision_crypto = decision_engine.make_decision(market_data_crypto, sentiment_scores_crypto)
    backtester.run_backtest(decision_crypto)

    # Passage d'ordre si décision validée pour crypto
    if decision_crypto['action'] == 'buy':
        trading_api_crypto.place_order(decision_crypto)

    # Exemple de workflow pour stocks
    market_data_stocks = trading_api_stocks.get_market_data()  # Fetch stock market data
    news_data_stocks = trading_api_stocks.get_news_data()  # Fetch stock news data
    sentiment_scores_stocks = sentiment_analyzer.analyze(news_data_stocks)
    decision_stocks = decision_engine.make_decision(market_data_stocks, sentiment_scores_stocks)
    backtester.run_backtest(decision_stocks)

    # Passage d'ordre si décision validée pour stocks
    if decision_stocks['action'] == 'buy':
        trading_api_stocks.place_order(decision_stocks)

if __name__ == "__main__":
    main()
