class LRUCache:

    def __init__(self, capacity: int):
        # Define values, O(n) space
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # Short-circuit if key does not exist
        if key not in self.cache:
            return -1

        # Otherwise, reinsert key back into dict to move up the key's priority,
        # O(n) work
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val

        # Return key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # First case, the size is not overbound and the key is not yet 
        # inserted, so insert the key and increase size, O(1) work
        if self.size < self.capacity and key not in self.cache:
            self.size = self.size + 1
            self.cache[key] = value
        # Second case, we update the value of the key (regardless of cache 
        # size), so delete and reinsert the key back with the updated value, 
        # O(1) work
        elif key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        # Lastly, we evict the least recently used k,v pair and insert the 
        # new pair
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value