class TimeMap:

    def __init__(self):
        # Define the data structure as a dictionary of dictionaries paired,
        # with a dictionary of ints, which has O(n * m) space
        self.values = dict()
        self.timestamps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize dict for a specific key if it doesn't exist, O(1) work
        if key not in self.values:
            self.values[key] = dict()
            self.timestamps[key] = []

        # Add value to the dict relating to the key with its timestamp, (1)
        # work
        self.values[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # If the key isn't valid, return early
        if key not in self.values:
            return ""

        # Alias the keys for better reference, O(1) work
        keys = self.timestamps[key]

        # Variables used to store intermediary states, O(1) work
        lo, hi = 0, len(keys) - 1
        max_timestamp = -1

        # Run binary search on the timestamps, and since there are n keys
        # associated with the timestamp, O(log n) work
        while lo <= hi:
            # Calculate midpoint, O(1) work
            mid = lo + (hi - lo) // 2

            # Usual binary search casing, O(1) work
            if keys[mid] == timestamp:
                return self.values[key][keys[mid]]
            elif keys[mid] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1

            # We want to save the biggest possible timestamp L.E.Q. to
            # timestamp, so we compute the max for each timestamp checked,
            # O(1) work
            if keys[mid] <= timestamp:
                max_timestamp = max(max_timestamp, keys[mid])

        return "" if max_timestamp == -1 or max_timestamp > timestamp \
                else self.values[key][max_timestamp]
