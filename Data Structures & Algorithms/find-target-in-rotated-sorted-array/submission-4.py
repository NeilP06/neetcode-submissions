class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Variables needed to track intermediary states, O(1) space
        lo_i, hi_i = 0, len(nums) - 1
        index = float("inf") # Used to store the pivot (min element index)
        min_num = float("inf")

        # Use binary search to find the pivot, e.g. the minimum element's
        # index, O(log n) work
        while lo_i <= hi_i:
            # Calculate midpoint, O(1) work
            mid = lo_i + (hi_i - lo_i) // 2

            # Search to the right if left is sorted correctly, else search
            # to the left, O(1) work
            if nums[mid] >= nums[lo_i] and nums[mid] > nums[hi_i]:
                lo_i = mid + 1
            else:
                hi_i = mid - 1

            # Store minimum element and its index if it applies, O(1) work
            if nums[mid] < min_num:
                min_num = nums[mid]
                index = mid

        # Variables needed to track intermediary states for the binary search
        # subproblems, O(1) space
        lo_l, hi_l = 0, index - 1
        lo_r, hi_r = index + 1, len(nums) - 1

        # Use binary search on the left subarray of the pivot to search for 
        # target, O(log n) work
        while lo_l <= hi_l:
            # Calculate midpoint, O(1) work
            mid = lo_l + (hi_l - lo_l) // 2

            # Usual binary search casing, O(1) work
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo_l = mid + 1
            else:
                hi_l = mid - 1

        # Use binary search on the right subarray of the pivot to search for 
        # target, O(log n) work
        while lo_r <= hi_r:
            # Calculate midpoint, O(1) work
            mid = lo_r + (hi_r - lo_r) // 2

            # Usual binary search casing, O(1) work
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo_r = mid + 1
            else:
                hi_r = mid - 1                

        # Return the pivot if the minimum element is the target else -1
        return index if nums[index] == target else -1