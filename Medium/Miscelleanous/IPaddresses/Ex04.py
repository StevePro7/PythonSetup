# 4. Finding the IP Address of a Hostname
import socket


def get_ip_from_hostname(hostname: str) -> str:
    try:
        return socket.gethostbyname(hostname)
    except ValueError:
        return "Invalid hostname"


print(get_ip_from_hostname("google.com"))
