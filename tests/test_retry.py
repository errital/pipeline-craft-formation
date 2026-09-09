from pathlib import Path

COUNTER_FILE = Path("/tmp/retry-demo")

def test_retry():
    if not COUNTER_FILE.exists():
        COUNTER_FILE.write_text("1")
        assert False 

    assert True
