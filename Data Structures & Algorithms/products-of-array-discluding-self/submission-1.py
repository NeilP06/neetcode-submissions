class Solution:
    # O(n) space, O(n) work
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space
        prefix = 1
        suffix = 1
        result = [1] * len(nums)

        # Build the prefixes product, O(n) work
        for i in range(len(nums)):
            if i == 0:
                result[0] = 1
                prefix *= nums[i]
                continue
            result[i] = prefix
            prefix *= nums[i]

        # Multiply by the suffixes product, O(n) work
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix *= nums[i]
                continue
            result[i] = result[i] * suffix
            suffix *= nums[i]

        return result