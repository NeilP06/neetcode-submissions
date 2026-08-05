class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t, h = nums[0], nums[0]

        while True:
            t = nums[t]
            h = nums[h]

            if t == nums[h]:
                return h
            
            h = nums[h]

        return -1