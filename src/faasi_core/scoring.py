class ScoreAggregator:
    WEIGHTS = {
        'task_success': 0.20,
        'tool_accuracy': 0.15,
        'recovery_quality': 0.15,
        'memory_integrity': 0.10,
        'safety_compliance': 0.10,
        'ambiguity_handling': 0.10,
        'stability': 0.10,
        'efficiency': 0.10,
    }

    @classmethod
    def composite_score(cls, metrics):
        return sum(metrics.get(k, 0) * w for k, w in cls.WEIGHTS.items())
