# WEnumerating Network Interfaces
import socket
import netifaces
for interface in netifaces.interfaces():
    addr = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
    if addr:
        print(f"Interface: {interface}, Address: {addr[0]['addr']}")
