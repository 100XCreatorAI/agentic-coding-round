import pytest

from src.main import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert "ready" in capsys.readouterr().out
