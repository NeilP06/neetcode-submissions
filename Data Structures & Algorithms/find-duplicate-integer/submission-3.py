class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t, h = nums[0], nums[0]

        while True:
            t = nums[t]
            h = nums[nums[h]]

            if t == h:
                verifier = nums[0]

                while verifier != t:
                    verifier = nums[verifier]
                    t = nums[t]

                return verifier

        return -1