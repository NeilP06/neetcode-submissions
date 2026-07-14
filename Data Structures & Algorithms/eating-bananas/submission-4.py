class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Variables needed to track intermediary states, O(1) space
        lo, hi = 1, max(piles)
        best = -1

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

            # Variables needed to track hours for the rates +/- 1 of mid, O(1)
            # space
            l = -1 if mid == 1 else mid - 1
            r = -1 if mid == max(piles) else mid + 1
            l_hours, r_hours = 0, 0

            # Use the same logic to calculate hours it takes for the rates +/- 
            # 1 of mid, O(n) work
            for pile in piles:
                l_time = pile//l if pile % l == 0 else pile // l + 1
                r_time = pile//r if pile % r == 0 else pile // r + 1

                l_hours += l_time
                r_hours += r_time

            # If both rates are less efficient than that of mid, we hit the min
            # rate, so return early
            if l_hours > hours and r_hours > hours:
                return mid

            # Else, use the binary search casing technique to narrow the search
            # range, O(1) work
            if hours <= h:
                best = mid
                hi = mid - 1
            elif hours > h:
                lo = mid + 1


        return best