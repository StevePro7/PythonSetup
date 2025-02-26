# 8 Generating a List of IPs in a Subnet
import ipaddress


def list_ips_in_subnet(subnet: str) -> list:
    try:
        return [str(ip) for ip in ipaddress.ip_network(subnet, strict=False)]
    except ValueError:
        return []


ips_list: list[str] = list_ips_in_subnet("192.168.1.0/30")
print(len(ips_list))
print(ips_list)
