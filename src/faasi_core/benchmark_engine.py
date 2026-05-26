from .task_loader import TaskLoader
from .evaluator_core import Evaluator
from .task_executor import TaskExecutor

class BenchmarkEngine:
    def run(self, task_file: str):
        tasks = TaskLoader.load_tasks(task_file)
        evaluator = Evaluator()
        executor = TaskExecutor()
        results = []
        for task in tasks:
            metrics = executor.execute(task)
            score = evaluator.evaluate(metrics)
            results.append({'task_id': task.task_id, 'category': task.category, 'score': score})
        return results
