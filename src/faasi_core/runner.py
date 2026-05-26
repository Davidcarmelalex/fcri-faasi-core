from .schemas import TaskDefinition, EvaluationResult

class BenchmarkRunner:
    def run_task(self, task: TaskDefinition) -> EvaluationResult:
        return EvaluationResult(task_id=task.task_id, success=False, score=0.0, notes='Runner scaffold initialized')
