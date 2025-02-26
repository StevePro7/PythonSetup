# 5.Pinging a Host
import subprocess


def ping_host(host: str) -> bool:
    try:
        output = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        return output.returncode == 0
    except subprocess.CalledProcessError:
        return False


print(ping_host("8.8.8.8"))  # Returns True if reachable
