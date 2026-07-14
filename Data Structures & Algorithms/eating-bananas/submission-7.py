class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Variables needed to track intermediary states, O(1) space
        lo, hi = 1, max(piles)
        best = float("inf")

        # Use binary search to find the minimum # bananas to eat in this
        # range, so O(log m) time
        while lo <= hi:
            # Variables needed to do logic inside the binary search loop, O(1)
            # space
            mid = lo + (hi - lo) // 2
            hours = 0

            # Calculate hours needed to eat all bananas at the defined pace set
            # by mid, O(n) work
            for pile in piles:
                time = pile // mid if pile % mid == 0 else pile // mid + 1
                hours += time

            # Else, use the binary search casing technique to narrow the search
            # range, O(1) work
            if hours <= h:
                best = min(best, mid)
                hi = mid - 1
            elif hours > h:
                lo = mid + 1

        return best