class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Variables needed to track intermediary states, O(1) space
        lo, hi = 0, len(nums) - 1
        res = float("inf")

        # Run binary search on the array, O(log n) work
        while lo <= hi:
            # Calculate midpoint without risking overflow, O(1) work
            mid = lo + (hi - lo) // 2

            # Here, we case to eventually shift the boundary to the split zone,
            # done by shifting right if we know the left is in order, and 
            # shifting left if we know that right is in order, taking the min
            # value of all explored ones, O(1) work
            if nums[lo] <= nums[mid] and nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
            res = min(res, nums[mid])

        return res