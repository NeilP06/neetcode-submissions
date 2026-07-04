class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Variable needed to track states, O(n) space
        states = dict()

        # Preprocessing before entering the loop, O(n log n) work
        nums = list(enumerate(nums))
        nums = sorted(nums, key=lambda x: x[1])

        # Iterate through the array linearly, where the first index acts as a 
        # pivot to find the second and third indices, O(n) work
        for first in range(len(nums)):
            # Reduce the problem to a Two Sum Sorted Array problem by setting
            # the target to the negative of first index's value
            target = -nums[first][1]

            # Variables needed to track the problem reduction
            second = 0 
            third = len(nums) - 1

            # Loop the second and third indices manually in a linear fashion,
            # O(n) work
            while second < third:
                # Prevent possible duplicate pair of indices
                if second == first:
                    second += 1
                    continue
                elif third == first:
                    third -= 1
                    continue 

                # Calculate the sum between the pair of the two free indices, 
                # O(1) work
                total = nums[second][1] + nums[third][1]
                
                # Use the sum to decide the logical action (e.g. move second
                # or third appropriately if the sum isn't equal, or add the 
                # key-indices to the states dict if it is a valid pair), O(1)
                # work
                if total < target:
                    second += 1
                elif total > target:
                    third -= 1
                else:
                    # Define the key to be the value pairs as a tuple (so that
                    # the key is hashable) and then add to dict, O(1) work
                    key = tuple(sorted([
                        nums[first][1], 
                        nums[second][1], 
                        nums[third][1]]
                    ))
                    if key not in states:
                        states[key] = True
                    
                    # Increment arbitrarily to avoid an infinite loop
                    second += 1

        # Build final result, O(n) work
        result = []
        for key in states.keys():
            result.append(list(key))

        return result