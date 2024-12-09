# 1. Use Strong Encryption Protocols (TLS 1.2+)
import ssl
import socket

# Create secure context TLS v1.2+
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

# Create secure connection
with socket.create_connection(('google.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='google.com') as secure_sock:
        secure_sock.sendall(b'Hello secure world')