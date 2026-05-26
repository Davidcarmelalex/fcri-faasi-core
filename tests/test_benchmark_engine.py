from faasi_core.benchmark_engine import BenchmarkEngine

def test_benchmark_engine_runs():
    engine = BenchmarkEngine()
    results = engine.run('examples/sample_tasks.json')
    assert len(results) > 0
