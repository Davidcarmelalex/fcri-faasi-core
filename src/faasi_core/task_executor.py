from .failure_modes import FailureInjector

class TaskExecutor:
    def execute(self, task):
        category = getattr(task, 'category', 'generic')
        if category == 'recovery':
            simulated = FailureInjector.inject_missing_file({'task_id': task.task_id})
            return {
                'task_success': 0.75,
                'tool_accuracy': 0.8,
                'recovery_quality': 0.95,
                'memory_integrity': 0.8,
                'safety_compliance': 1.0,
                'ambiguity_handling': 0.85,
                'stability': 0.8,
                'efficiency': 0.7,
                'simulation': simulated,
            }
        return {
            'task_success': 0.9,
            'tool_accuracy': 0.85,
            'recovery_quality': 0.75,
            'memory_integrity': 0.8,
            'safety_compliance': 1.0,
            'ambiguity_handling': 0.8,
            'stability': 0.85,
            'efficiency': 0.8,
        }
