class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = dict()
        starters = dict()

        for num in nums:
            if num not in cache:
                cache[num] = True
            
        for num in nums:
            if num - 1 not in cache:
                starters[num] = 1

        for start in starters.keys():
            current = start + 1
            while current in cache:
                starters[start] += 1
                current += 1     

        max_streak = 0
        
        for start in starters.keys():
            streak = starters[start]

            max_streak = max_streak if max_streak > streak else streak

        return max_streak