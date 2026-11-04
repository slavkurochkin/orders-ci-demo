import sys


def test_fails_only_on_python_313():
    # Probe: one matrix leg goes red, to see what the aggregate check reports.
    assert sys.version_info < (3, 13), "deliberately red on 3.13"
