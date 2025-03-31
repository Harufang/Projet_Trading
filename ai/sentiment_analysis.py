from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased")

    def analyze(self, news_data):
        # ...existing code...
        results = []
        for news in news_data:
            sentiment = self.model(news['title'])
            results.append({"title": news['title'], "sentiment": sentiment[0]})
        return results
