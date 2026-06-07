class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = dict()
        d_t = dict()

        for char in s:
            if char not in d_s:
                d_s[char] = 1
            else:
                d_s[char] += 1

        for char in t:
            if char not in d_t:
                d_t[char] = 1
            else:
                d_t[char] += 1

        d = d_s if len(s) > len(t) else d_t

        for key in d.keys():
            if key not in d_t or key not in d_s:
                return False
            elif d_s[key] != d_t[key]:
                return False
        
        return True