"""Report runner used by the synthetic review fixture."""

import subprocess


def run_report(command: str) -> str:
    """Run a report command and return its standard output."""
    completed = subprocess.run(
        command,
        shell=True,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout
