class TimeMap:

    def __init__(self):
        # Define the datastructure as a dictionary of dictionaries,
        # which has O(n * m) space
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize dict for a specific key if it doesn't exist, O(1) work
        if key not in self.values:
            self.values[key] = dict()
        # Add value to the dict relating to the key with its timestamp, (1)
        # work
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.values:
        #     return ""

        keys = list(self.values[key].keys())
        print(keys)

        lo, hi = 0, len(keys) - 1
        max_timestamp = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if keys[mid] == timestamp:
                return self.values[key][keys[mid]]
            elif keys[mid] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1

            if keys[mid] <= timestamp:
                max_timestamp = max(max_timestamp, keys[mid])

        return "" if max_timestamp == -1 or max_timestamp > timestamp else self.values[key][max_timestamp]
