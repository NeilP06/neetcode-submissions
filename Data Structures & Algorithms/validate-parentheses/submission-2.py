class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Extra variable to make casing convenient
        opens = { "(", "{", "["}

        # Run through the string linearly, O(n) work
        for bracket in s:
            # Add only open strings to the stack, O(1) work
            if bracket in opens:
                stack.append(bracket)
            # Else case on specific brackets and do the ideal action, O(1) work
            elif bracket == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            elif bracket == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            elif bracket == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
                        
        return len(stack) == 0