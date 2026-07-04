class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        lo = 0
        hi = len(heights) - 1

        while lo < hi:
            width = hi - lo
            area = width * min(heights[lo], heights[hi])
            result = max(result, area)

            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        return result