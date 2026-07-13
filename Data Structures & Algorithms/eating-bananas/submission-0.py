class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, max(piles)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            hours = 0

            for pile in piles:
                time = pile//mid if pile % mid == 0 else pile // mid + 1
                hours += time

            print(mid, hours)

            if hours <= h:
                return mid
            else:
                lo = mid + 1

            

        return -1
            