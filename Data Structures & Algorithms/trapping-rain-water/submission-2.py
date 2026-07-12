class Solution:
    def trap(self, height: List[int]) -> int:
        # Variables needed to store intermediate states and final result, O(n)
        # space
        result = 0
        prefixes = [0] * len(height)
        suffixes = [0] * len(height)

        # Iterate through the array once, O(n) work
        for i in range(len(height)):
            # Compute the corresponding index when going in reverse order, O(1)
            # work
            j = len(height) - 1 - i

            # Base case, O(1) work
            if i == 0:
                prefixes[i] = height[i]
                suffixes[j] = height[j]
                continue

            # Recurrence, O(1) work
            prefixes[i] = max(prefixes[i - 1], height[i])
            suffixes[j] = max(suffixes[j + 1], height[j])

        # Calculate sum by using formula min(suffix, prefix) - height (making
        # sure that it is positive), O(n) work
        for i in range(len(height)):
            result += max(0, min(suffixes[i], prefixes[i]) - height[i])

        return result
