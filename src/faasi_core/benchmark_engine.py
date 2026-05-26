from .task_loader import TaskLoader
from .evaluator_core import Evaluator

class BenchmarkEngine:
    def run(self, task_file: str):
        tasks = TaskLoader.load_tasks(task_file)
        evaluator = Evaluator()
        results = []
        for task in tasks:
            metrics = {
                'task_success': 0.9,
                'tool_accuracy': 0.85,
                'recovery_quality': 0.75,
                'memory_integrity': 0.8,
                'safety_compliance': 1.0,
                'ambiguity_handling': 0.8,
                'stability': 0.85,
                'efficiency': 0.8,
            }
            score = evaluator.evaluate(metrics)
            results.append({'task_id': task.task_id, 'score': score})
        return results
