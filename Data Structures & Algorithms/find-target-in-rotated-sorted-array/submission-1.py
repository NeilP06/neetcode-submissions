class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[mid] and nums[lo] <= target and nums[mid] > target:
                hi = mid - 1
            elif nums[mid] > target:
                lo = mid + 1
            elif nums[mid] < target and nums[mid] <= nums[hi] and target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1