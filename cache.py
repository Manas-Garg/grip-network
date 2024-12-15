import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Caching functions
def set_cache(key, value, ttl=3600):
    cache.setex(key, ttl, value)

def get_cache(key):
    return cache.get(key)

# Example usage
if __name__ == "__main__":
    set_cache("prediction", "123.45")
    print("Cached value:", get_cache("prediction"))
