class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.strip()

        while i < j:
            if not s[i].isalpha() and not s[i].isnumeric():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
                continue
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True