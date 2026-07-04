class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Variables needed to track intermediate states and final result, O(1)
        # space
        result = 0
        lo, hi = 0, len(heights) - 1

        # Loop through the array using two pointers, O(n) work
        while lo < hi:
            # Calculate the area of the rectangle and set result to the max
            # current rectangle, O(1) work
            area = (hi - lo) * min(heights[lo], heights[hi])
            result = max(result, area)

            # Shift the pointers depending on which index's value is smaller
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        return result