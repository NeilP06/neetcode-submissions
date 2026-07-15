class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo_i, hi_i = 0, len(nums) - 1
        index = float("inf")
        min_num = float("inf")

        while lo_i <= hi_i:
            mid = lo_i + (hi_i - lo_i) // 2

            if nums[mid] >= nums[lo_i] and nums[mid] > nums[hi_i]:
                lo_i = mid + 1
            else:
                hi_i = mid - 1

            if nums[mid] < min_num:
                min_num = nums[mid]
                index = mid

        lo_l, hi_l = 0, index - 1
        lo_r, hi_r = index + 1, len(nums) - 1

        while lo_l <= hi_l:
            mid = lo_l + (hi_l - lo_l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo_l = mid + 1
            else:
                hi_l = mid - 1

        while lo_r <= hi_r:
            mid = lo_r + (hi_r - lo_r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo_r = mid + 1
            else:
                hi_r = mid - 1                

        return index if nums[index] == target else -1