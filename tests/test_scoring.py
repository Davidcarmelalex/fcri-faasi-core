from src.faasi_core.scoring import ScoreAggregator

def test_composite_score_range():
    metrics = {
        'task_success': 1.0,
        'tool_accuracy': 1.0,
        'recovery_quality': 1.0,
        'memory_integrity': 1.0,
        'safety_compliance': 1.0,
        'ambiguity_handling': 1.0,
        'stability': 1.0,
        'efficiency': 1.0,
    }
    assert ScoreAggregator.composite_score(metrics) == 1.0
