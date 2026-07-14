class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        best = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if mid == 0:
                return best
            hours = 0

            for pile in piles:
                time = pile//mid if pile % mid == 0 else pile // mid + 1
                hours += time

            print(mid, hours)

            if hours < h:
                best = mid
                hi = mid - 1
            elif hours > h:
                lo = mid + 1
            else:
                return mid

        return best