# 6.Setting a Ping Timeout
import subprocess


def ping_with_timeout(host, timeout=2):
    try:
        output = subprocess.run(["ping", "-c", "1", "-W", str(timeout), host], capture_output=True, text=True)
        return output.returncode == 0
    except subprocess.CalledProcessError:
        return False


print(ping_with_timeout("8.8.8.8", timeout=1))  # Adjust timeout as needed
