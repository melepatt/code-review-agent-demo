import subprocess

ALLOWED = {"status": ["git", "status", "--short"]}

def run_allowed(name: str) -> int:
    command = ALLOWED.get(name)
    if command is None:
        raise ValueError("unknown command")
    return subprocess.run(command, shell=False, check=False).returncode
