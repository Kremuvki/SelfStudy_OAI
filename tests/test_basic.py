"""Basic tests to ensure the testing framework is working."""

import sys
from pathlib import Path

import pytest

# Add the project root to the path so we can import modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_python_version():
    """Test that we're using a supported Python version."""
    assert sys.version_info >= (3, 8), "Python 3.8+ is required"


def test_imports():
    """Test that essential packages can be imported."""
    try:
        import jupyter  # noqa: F401
        import matplotlib  # noqa: F401
        import numpy  # noqa: F401
        import pandas  # noqa: F401
        import seaborn  # noqa: F401
        import sklearn  # noqa: F401
    except ImportError as e:
        pytest.fail(f"Failed to import essential package: {e}")


def test_project_structure():
    """Test that the project structure is correct."""
    project_root = Path(__file__).parent.parent

    # Check essential directories exist
    assert (project_root / "problems").exists()
    assert (project_root / "scripts").exists()
    assert (project_root / "tests").exists()
    assert (project_root / ".github" / "workflows").exists()

    # Check essential files exist
    assert (project_root / "README.md").exists()
    assert (project_root / "requirements.txt").exists()
    assert (project_root / "pyproject.toml").exists()


if __name__ == "__main__":
    pytest.main([__file__])
