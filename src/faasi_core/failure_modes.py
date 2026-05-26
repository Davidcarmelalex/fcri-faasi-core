class FailureInjector:
    @staticmethod
    def inject_missing_file(task: dict) -> dict:
        task = dict(task)
        task['failure_mode'] = 'missing_file'
        return task
