from pathlib import Path
import tempfile


def test_retry():
    counter_file = Path(tempfile.gettempdir()) / "retry-demo"

    if not counter_file.exists():
        counter_file.write_text("1")
        raise AssertionError("Échec volontaire pour tester le retry")

    assert True