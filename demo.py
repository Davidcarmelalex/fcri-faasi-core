from faasi_core.scoring import ScoreAggregator
from faasi_core.reporting import ReportGenerator

metrics = {
    'task_success': 1.0,
    'tool_accuracy': 0.9,
    'recovery_quality': 0.7,
    'memory_integrity': 0.8,
    'safety_compliance': 1.0,
    'ambiguity_handling': 0.8,
    'stability': 0.9,
    'efficiency': 0.75,
}

score = ScoreAggregator.composite_score(metrics)
print(ReportGenerator().summary(score))
