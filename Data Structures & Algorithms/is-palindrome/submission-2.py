class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Variables needed to maintain states
        i, j = 0, len(s) - 1
        s = s.strip()

        # Loop with one going left to right and another going right to left,
        # O(n) work
        while i < j:
            # Check if any of the current indices point to a valid ASCII char;
            # if not, skip it
            if not s[i].isalpha() and not s[i].isnumeric():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
                continue
            
            # Maintain palindrome constraint
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True