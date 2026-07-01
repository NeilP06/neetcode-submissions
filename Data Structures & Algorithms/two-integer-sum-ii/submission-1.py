class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Variables needed to track states and result, O(1) space
        lo, hi = 0, len(numbers) - 1

        # Use two points to take advantage of the sorted input to find the
        # valid pair, O(n) work
        while lo < hi:
            curr = numbers[lo] + numbers[hi]

            # Handle all 3 cases, O(1) work
            if curr > target:
                hi -= 1
            elif curr < target:
                lo += 1
            else:
                return [lo + 1, hi + 1]

        return [-1, -1]
            