class Solution:
    # O(n) space, O(n) work
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space
        prefix = 1
        suffix = 1
        result = [1] * len(nums)

        # Build the prefixes product, O(n) work
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Multiply by the suffixes product, O(n) work
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]

        return result