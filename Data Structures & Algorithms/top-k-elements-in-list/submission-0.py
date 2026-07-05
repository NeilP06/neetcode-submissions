class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        res = []

        # Temporary counters
        prev = nums[0]
        prev_count = 1


        # O(n) work -- sweep through the array once to get frequencies
        for i in range(1, len(nums), 1):
            if nums[i] != prev:
                if prev_count not in counts:
                    counts[prev_count] = [prev]
                else:
                    counts[prev_count].append(prev)
                
                prev = nums[i]
                prev_count = 1
            else:
                prev_count += 1

        if prev_count not in counts:
            counts[prev_count] = [prev]
        else:
            counts[prev_count].append(prev)
        
        # O(??) work
        keys = sorted(counts.keys(), reverse=True)

        numLeft = k
        print(keys)

        for key in keys:
            if numLeft == 0:
                break
            
            values = counts[key]

            for val in values:
                if numLeft == 0:
                    break

                res.append(val)
                numLeft -= 1

        return res