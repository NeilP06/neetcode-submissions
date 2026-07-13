class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Values needed to track intermediary states, O(1) space
        lo, hi = 0, len(nums) - 1

        # The search space is halved each time, so the loop runs in O(log n)
        # work
        while lo <= hi:
            # Calculate the midpoint, O(1) work
            mid = (lo + hi) // 2

            # Adjust pointers or return result based on case, O(1) work
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1