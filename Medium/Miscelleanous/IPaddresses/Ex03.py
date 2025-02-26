# 3. Getting the Hostname from an IP Address
import socket


def get_hostname(ip: str) -> (str, list[str]):
    try:
        return socket.gethostbyaddr(ip)
    except ValueError:
        return "Host not found"


print(get_hostname("8.8.8.8"))  # Google's public DNS
