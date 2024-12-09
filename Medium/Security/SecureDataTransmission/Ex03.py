# 3. Encrypt Sensitive Data Before Transmission
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b'sixteen byte key'
iv = b'sixteen byte iv..'
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

encyptor = cipher.encryptor()
ciphertext = encyptor.update(b'sensitive data') + encyptor.finalize()