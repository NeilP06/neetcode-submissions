class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        # O(m) for the outer loop
        for string in strs:
            temp_counter = dict()
            alias = ""

            # O(n) -- count # occurrences for each letter in the string
            for char in string:
                temp_counter[char] = 1 + temp_counter.get(char, 0)

            # O(1) -- there are a fixed # of keys for the dict (26 letters)
            for key in sorted(temp_counter.keys()):
                alias += key + str(temp_counter[key])

            if alias not in anagrams:
                anagrams[alias] = [string]
            else:
                anagrams[alias].append(string)

        # O(m) time to convert the values of a dict into a list
        return list(anagrams.values())