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

            left = -1 if mid == 1 else mid - 1
            right = -1 if mid == max(piles) else mid + 1
            left_hours, right_hours = 0, 0

            for pile in piles:
                left_time = pile//left if pile % left == 0 else pile // left + 1
                right_time = pile//right if pile % right == 0 else pile // right + 1

                left_hours += left_time
                right_hours += right_time

            if left_hours > hours and right_hours > hours:
                return mid


            if hours <= h:
                best = mid
                hi = mid - 1
            elif hours > h:
                lo = mid + 1


        return best