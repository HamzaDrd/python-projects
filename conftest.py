"""Lets every project keep its own simple `main.py` + `test_main.py`.

Before pytest imports a project's test file, that project's folder is put on the import
path and any `main` module from a previous project is forgotten, so `from main import ...`
always finds the right file.
"""

import sys
from pathlib import Path

import pytest


def pytest_collectstart(collector):
    if isinstance(collector, pytest.Module):
        sys.modules.pop("main", None)
        sys.path.insert(0, str(Path(collector.path).parent))


def pytest_collectreport(report):
    folder = str(Path(report.nodeid.split("::")[0]).resolve().parent)
    if folder in sys.path:
        sys.path.remove(folder)
