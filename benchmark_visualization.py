import json
from pathlib import Path

path = Path('benchmark_results.json')
if path.exists():
    data = json.loads(path.read_text(encoding='utf-8'))
    avg = sum(item['score'] for item in data) / len(data)
    print({'average_score': avg, 'tasks': len(data)})
else:
    print('No benchmark_results.json found')
