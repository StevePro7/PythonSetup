# 1. Checking if an IP Address is Private
import ipaddress


def check_private_ip(_ip: str) -> bool:
    try:
        ip_obj = ipaddress.ip_address(_ip)
        return ip_obj.is_private
    except ValueError:
        return False


ip: str = "192.168.0.1"
is_private: bool = check_private_ip(ip)
print(f"Is {ip} private? {is_private}")
