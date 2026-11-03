import subprocess

def run_archive(command: str) -> int:
    return subprocess.run(command, shell=True, check=False).returncode
