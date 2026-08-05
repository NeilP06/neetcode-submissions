class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Variables needed to track intermediary states, O(1) space
        t, h = nums[0], nums[0]

        # There is no condition for the tortoise-and-hare algorithm to stop, 
        # so loop infinitely, but since a cycle exists, the loop will return
        # early, in O(n) work
        while True:
            # Hare goes twice as far as tortoise
            t = nums[t]
            h = nums[nums[h]]

            # Once the meeting point is found, stop updating the hare pointer
            if t == h:
                # Initialize another slow pointer
                verifier = nums[0]

                # Move both pointers by one until they meet, where it is 
                # mathematically guaranteed this is the start of the cycle,
                # O(n) work (not mulitiplied by the outer O(n))
                while verifier != t:
                    verifier = nums[verifier]
                    t = nums[t]

                # The start of the cycle represents the repeating number
                return verifier

        # Unreachable
        return -1