from faasi_core.benchmark_engine import BenchmarkEngine

engine = BenchmarkEngine()
results = engine.run('examples/sample_tasks.json')
print(results)
