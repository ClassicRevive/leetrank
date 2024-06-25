from functools import lru_cache

@lru_cache(maxsize=None)
def test():
    return [3]

print(test())