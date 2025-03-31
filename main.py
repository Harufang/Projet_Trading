from api.trading_api import TradingAPI, InteractiveBrokersAPI
from ai.sentiment_analysis import SentimentAnalyzer
from ai.decision_engine import DecisionEngine
from ai.backtesting import Backtester
from config.settings import API_KEYS, IB_CONFIG, TWILIO_CONFIG
from ui.visual_interface import TradingInterface
from notifications.whatsapp import WhatsAppNotifier

def main():
    # Initialisation des modules
    trading_api_crypto = TradingAPI(API_KEYS['crypto'])
    ib_api = InteractiveBrokersAPI(**IB_CONFIG)
    sentiment_analyzer = SentimentAnalyzer()
    decision_engine = DecisionEngine()
    backtester = Backtester()
    ui = TradingInterface()
    notifier = WhatsAppNotifier(**TWILIO_CONFIG)

    # Exemple de workflow pour crypto
    market_data_crypto = trading_api_crypto.get_market_data()
    news_data_crypto = trading_api_crypto.get_news_data()
    sentiment_scores_crypto = sentiment_analyzer.analyze(news_data_crypto)
    decision_crypto = decision_engine.make_decision(market_data_crypto, sentiment_scores_crypto)
    backtester.run_backtest(decision_crypto)

    if decision_crypto['action'] == 'buy':
        trading_api_crypto.place_order(decision_crypto)
        notifier.send_message(f"Crypto Buy Order Placed: {decision_crypto}")

    # Update UI with crypto data
    ui.update_activity("Crypto", market_data_crypto, decision_crypto)

    # Exemple de workflow pour stocks via Interactive Brokers
    market_data_stocks = ib_api.get_market_data("AAPL")  # Fetch stock market data
    news_data_stocks = trading_api_crypto.get_news_data()  # Reuse news fetching for stocks
    sentiment_scores_stocks = sentiment_analyzer.analyze(news_data_stocks)
    decision_stocks = decision_engine.make_decision(market_data_stocks, sentiment_scores_stocks)
    backtester.run_backtest(decision_stocks)

    if decision_stocks['action'] == 'buy':
        ib_api.place_order("AAPL", decision_stocks['action'], decision_stocks['amount'])
        notifier.send_message(f"Stock Buy Order Placed: {decision_stocks}")

    # Update UI with stock data
    ui.update_activity("Stocks", market_data_stocks, decision_stocks)

    # Start the UI loop
    ui.run()

if __name__ == "__main__":
    main()
