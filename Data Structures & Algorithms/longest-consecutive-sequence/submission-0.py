class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = dict()

        for num in nums:
            is_in = False
            for start in cache.keys():
                previous, counter = cache[start]

                if num == previous + 1:
                    cache[start] = [num, counter + 1]
                    is_in = True

            if not is_in:
                cache[num] = [num, 1]

        max_streak = float("-inf")
        
        for start in cache.keys():
            previous, streak = cache[start]

            max_streak = max_streak if max_streak > streak else streak

        return max_streak