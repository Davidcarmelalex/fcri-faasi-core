from src.faasi_core.schemas import TaskDefinition
from src.faasi_core.runner import BenchmarkRunner

task = TaskDefinition(
    task_id='demo-001',
    category='tool_reliability',
    prompt='Demo benchmark execution',
    metadata={}
)

result = BenchmarkRunner().run_task(task)
print(result)
