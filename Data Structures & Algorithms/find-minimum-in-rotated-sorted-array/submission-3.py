class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Variables needed to track intermediary states, O(1) space
        lo, hi = 0, len(nums) - 1
        res = float("inf")

        # Run binary search on the array, O(log n) work
        while lo <= hi:
            mid = lo + (hi - lo) // 2


            if nums[lo] <= nums[mid] and nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
            
            res = min(res, nums[mid])

        return min(res, nums[mid])