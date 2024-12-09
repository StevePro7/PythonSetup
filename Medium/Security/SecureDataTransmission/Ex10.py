# 2. Mutual TLS (mTLS) for Microservices
import socket
import ssl

# Create SSL context with client authentication
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='client-cert.pem', keyfile='client-key.pem')
context.load_verify_locations(cafile='server-cert.pem')

# Connect to the server
with socket.create_connection(('server.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='server.com') as secure_sock:
        secure_sock.sendall(b'Hello, secure microservice')