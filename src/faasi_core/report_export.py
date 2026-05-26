import json

class ReportExporter:
    @staticmethod
    def export(results, path='benchmark_results.json'):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
