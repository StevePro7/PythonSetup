import time

from cachetools import TTLCache, cached

cache = TTLCache(maxsize=1000, ttl=300)  # Cache up to 1000 items, with a TTL of 5 minutes

@cached(cache)
def compute_expensive_operation(param):
    # Perform an expensive calculation or DB query here
    result = time.sleep(10000)
    return result