class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        prefixes = [0] * len(height)
        suffixes = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                prefixes[0] = height[0]
                suffixes[len(height) - 1] = height[len(height) - 1]
                continue

            prefixes[i] = max(prefixes[i - 1], height[i])
            suffixes[len(height) - 1 - i] = max(suffixes[len(height) - i], height[len(height) - 1 - i])

        result = 0
        for i in range(len(height)):
            result += max(0, min(suffixes[i], prefixes[i]) - height[i])

        return result
