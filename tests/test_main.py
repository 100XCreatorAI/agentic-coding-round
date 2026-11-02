from src.main import main


def test_main_runs(capsys):
    main()
    assert "ready" in capsys.readouterr().out
