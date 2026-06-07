class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = dict()
        
        # O(n) -- iterate over possible pairs linearly and aggregate to
        # dict if necessary (no wasting space)
        for i in range(len(nums)):
            remaining = target - nums[i]

            # Prevent invalid cases
            if remaining not in kv or kv[remaining] == i:
                kv[nums[i]] = i
                continue
            
            j = kv[remaining]

            ind1 = min(i, j)
            ind2 = max(i, j)

            return [ind1, ind2]

        return [-1, -1]
        