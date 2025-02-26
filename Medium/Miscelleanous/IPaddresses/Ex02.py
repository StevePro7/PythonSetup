# 2. Validating an IP Address
import ipaddress


def validate_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


print(validate_ip("256.100.50.25"))  # Invalid IP, returns False
print(validate_ip("192.168.1.1"))    # Valid IP, returns True
