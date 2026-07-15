class TimeMap:

    def __init__(self):
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = dict()
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        keys = list(self.values[key].keys())
        print(keys)

        lo, hi = 0, len(keys) - 1
        max_timestamp = float("-inf")

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if keys[mid] == timestamp:
                return self.values[key][keys[mid]]
            elif keys[mid] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
            max_timestamp = max(max_timestamp, keys[mid])

        return "" if max_timestamp > timestamp else self.values[key][max_timestamp]
