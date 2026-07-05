class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = dict()

        # O(n) 
        for i in range(len(nums)):
            kv[nums[i]] = i
        
        # O(n) 
        for j in range(len(nums) - 1, -1, -1):
            remaining = target - nums[j]

            if remaining not in kv:
                continue
            
            i = kv[remaining]

            ind1 = min(i, j)
            ind2 = max(i, j)

        return [ind1, ind2]
        