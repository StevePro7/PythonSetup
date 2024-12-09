# 1. End-to-End Encryption (E2EE)
from nacl.public import PrivateKey, Box

# Generate private keys for sender and recipient
sender_private_key = PrivateKey.generate()
recipient_private_key = PrivateKey.generate()

# Exchange public keys
sender_public_key = sender_private_key.public_key
recipient_public_key = recipient_private_key.public_key

# Create a secure Box for encryption
box = Box(sender_private_key, recipient_public_key)

# Encrypt the message
encrypted = box.encrypt(b'Hello, this is a secure message')

# Decrypt the message
box = Box(recipient_private_key, sender_public_key)
decrypted = box.decrypt(encrypted)