"""
The quick brown fox jumps over the lazy dog.
Run the numbered Contract and Swap teaching example.

Suggested reading order: see 00_start_here.md.

Run everything:
    python .\\class_example.py

Run tests only:
    python .\\class_example.py test

Run the demonstration only:
    python .\\class_example.py demo

Show the World Bible only:
    python .\\class_example.py bible
"""

import sys
import unittest

import step_07_tests
from step_08_demo import run_demonstration
from step_09_world_bible import display_world_bible


def run_tests() -> unittest.result.TestResult:
    """Load and run the tests collected in step 7."""
    suite = unittest.defaultTestLoader.loadTestsFromModule(step_07_tests)
    return unittest.TextTestRunner(verbosity=2).run(suite)


def print_usage() -> None:
    """Show the available commands."""
    print("Usage: python class_example.py [all|test|demo|bible]")


def main() -> None:
    """Run the selected parts of the example."""
    command = sys.argv[1].lower() if len(sys.argv) > 1 else "all"
    if command not in {"all", "test", "tests", "demo", "bible"}:
        print_usage()
        raise SystemExit(2)

    if command in {"all", "test", "tests"}:
        if not run_tests().wasSuccessful():
            raise SystemExit(1)

    if command == "all":
        run_demonstration()
        display_world_bible()
    elif command == "demo":
        run_demonstration()
    elif command == "bible":
        display_world_bible()


if __name__ == "__main__":
    main()
