import argparse
from .scoring import ScoreAggregator


def main():
    parser = argparse.ArgumentParser(description='FAASI-CORE CLI')
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    if args.demo:
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
        print(ScoreAggregator.composite_score(metrics))

if __name__ == '__main__':
    main()
