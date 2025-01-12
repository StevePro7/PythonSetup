# 7. Generate a Random Password
import random
import string

password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print(password)
