class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space -- indexed by characters, 26 of them
        vocab_s = dict()
        vocab_t = dict()

        # O(m) work
        for char in s:
            if char not in vocab_s:
                vocab_s[char] = 1
            else:
                vocab_s[char] += 1

        # O(n) work
        for char in t:
            if char not in vocab_t:
                vocab_t[char] = 1
            else:
                vocab_t[char] += 1

        # Early check of nonsimiliarity
        if len(vocab_s.keys()) != len(vocab_t.keys()):
            return False
        
        # O(n) = O(m) work if the check passes
        for key in vocab_s.keys():
            if key not in vocab_t:
                return False
            if vocab_s[key] != vocab_t[key]:
                return False

        return True