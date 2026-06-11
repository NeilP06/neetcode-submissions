class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Necessary data structures
        counts = dict()
        kv = [[] for _ in range(len(nums))] # O(n) space predefined
        result = []

        # O(n) -- get counts of each letter occurrence in a single sweep
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # O(n) outer loop -- if each num is distinct, there are O(n) keys
        for key in counts.keys():
            val = counts[key] - 1

            # O(1) to aggregate information into the key-value array
            kv[val].append(key)

        # O(k) to print final result, and as k <= n, O(n) to print final result
        numLeft = k
        for key in range(len(kv) - 1, -1, -1):
            if numLeft == 0:
                break
            
            values = kv[key]

            for val in values:
                if numLeft == 0:
                    break

                result.append(val)
                numLeft -= 1

        return result