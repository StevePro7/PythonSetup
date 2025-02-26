# 7 Checking if an IP Belongs to a Subnet
import ipaddress


def check_ip_in_subnet(ip, subnet: str) -> bool:
    try:
        return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet, strict=False)
    except ValueError:
        return False


print(check_ip_in_subnet("192.168.1.100", "192.168.1.0/24"))  # True
print(check_ip_in_subnet("192.168.2.100", "192.168.1.0/24"))  # False
