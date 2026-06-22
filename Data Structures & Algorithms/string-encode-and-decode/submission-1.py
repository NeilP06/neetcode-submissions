class Solution:

    def encode(self, strs: List[str]) -> str:
        result : str = ""
        lengths : str = ""

        for string in strs:
            result += string
            lengths += str(len(string)) + ","

        # Add delimiter " " to separate lengths + result
        result = lengths + " " + result 

        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        lengths, words = s.split(" ", 1)
        lengths = lengths.split(",")[:-1]
        accum = []
        index = s.find(" ") + 1

        for length in lengths:
            length = int(length)
            accum.append(s[index:index + length])
            index += length

        return accum