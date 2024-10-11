import timeit


setup = """
import random
import string
"""
stmt = """
def get_random_token(n_length: int) -> str:
	chars = string.ascii_uppercase + string.digits
	token = ''.join(random.choice(chars) for _ in range(n_length))
	return token
get_random_token(100)
"""
times = timeit.repeat(stmt=stmt, setup=setup, repeat=2, number=1000)
print(times)
