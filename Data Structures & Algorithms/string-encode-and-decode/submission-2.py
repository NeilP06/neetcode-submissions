class Solution:

    # O(n) runtime with O(m + n) space used
    def encode(self, strs: List[str]) -> str:
        # Two strings to track accumulated amount + length of each word
        result : str = ""
        lengths : str = ""
        
        # O(n) work to aggregate all strings
        for string in strs:
            result += string
            lengths += str(len(string)) + ","

        # Add delimiter " " to separate lengths + result
        result = lengths + " " + result 

        return result

    def decode(self, s: str) -> List[str]:
        # Split and sanitize inputs into word lengths + aggregated string
        lengths, words = s.split(" ", 1)
        lengths = lengths.split(",")[:-1]

        # Vars to track output
        accum = []
        index = s.find(" ") + 1

        # O(n) work for the loop
        for length in lengths:
            # Use known info to extract individual strings, which is O(1) time
            length = int(length)
            accum.append(s[index:index + length])
            index += length

        return accum