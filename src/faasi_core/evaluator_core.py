from .scoring import ScoreAggregator

class Evaluator:
    def evaluate(self, metrics: dict) -> float:
        return ScoreAggregator.composite_score(metrics)
