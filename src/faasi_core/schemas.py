from dataclasses import dataclass
from typing import Dict

@dataclass
class TaskDefinition:
    task_id: str
    category: str
    prompt: str
    metadata: Dict

@dataclass
class EvaluationResult:
    task_id: str
    success: bool
    score: float
    notes: str = ""
