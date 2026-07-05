class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Variables needed to track states and final result
        lo, hi = 0, len(nums) - 1
        result = dict()

        # Preprocessing before entering the loop, O(n log n) work
        nums = list(enumerate(nums))
        nums = sorted(nums, key=lambda x: x[1])
        print(nums)

        # Use a two pointer strategy to fix two out of the three indices while
        # searching, O(n) work
        while lo < hi:
            closest = float("inf")
            # Use the "free" pointer to search for possible triplets, O(n) work
            for mid in range(len(nums)):
                if mid != lo and mid != hi:
                    curr = nums[lo][1] + nums[mid][1] + nums[hi][1]

                    if curr == 0:
                        candidate = tuple(sorted([nums[lo][1], nums[mid][1], nums[hi][1]]))
                        if candidate not in result:
                            result[candidate] = True
                        closest = 0
                    else:
                        closest = curr if abs(curr) < abs(closest) else closest

            if closest < 0:
                lo += 1
            else:
                hi -= 1

        trueres = []
        for key in result.keys():
            trueres.append(list(key))
        return trueres