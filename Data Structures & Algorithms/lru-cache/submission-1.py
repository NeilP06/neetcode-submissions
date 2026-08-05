class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        print(key, value, self.size)
        if self.size < self.capacity and key not in self.cache:
            self.size = self.size + 1
            self.cache[key] = value
        elif key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value