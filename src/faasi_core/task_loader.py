import json
from pathlib import Path
from .schemas import TaskDefinition

class TaskLoader:
    @staticmethod
    def load_tasks(path: str):
        data = json.loads(Path(path).read_text(encoding='utf-8'))
        return [TaskDefinition(**task) for task in data]
