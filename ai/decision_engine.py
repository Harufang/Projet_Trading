class DecisionEngine:
    def __init__(self):
        # ...existing code...
        pass

    def make_decision(self, market_data, sentiment_scores):
        # ...existing code...
        # Exemple : logique simple pour décider d'acheter ou vendre
        if sentiment_scores[0]['sentiment']['label'] == 'POSITIVE':
            return {"action": "buy", "amount": 100}
        return {"action": "hold"}
