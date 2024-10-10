from urllib.parse import urlparse


uri = urlparse('https://john:qwer1234@127.0.0.1:5672/convert-pdf-to-txt?admin=true')

print(uri)

print(uri.scheme)
print(uri.username)
print(uri.password)
print(uri.hostname)
print(uri.port)