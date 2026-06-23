class Solution:
    # O(n) space, O(n) work
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        result = [1] * len(nums)

        # Build the prefixes product, O(n) work
        for i in range(len(nums)):
            if i == 0:
                prefixes[i] = nums[0]
                continue
            prefixes[i] = prefixes[i - 1] * nums[i]

        # Build the suffixes product, O(n) work
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffixes[i] = nums[len(nums) - 1]
                continue
            suffixes[i] = suffixes[i + 1] * nums[i]

        # Build the resulting array, O(n) work
        for i in range(len(nums)):
            if i == 0:
                result[i] = suffixes[i + 1]
            elif i == len(nums) - 1:
                result[i] = prefixes[i - 1]
            else:
                result[i] = prefixes[i - 1] * suffixes [i + 1]

        return result