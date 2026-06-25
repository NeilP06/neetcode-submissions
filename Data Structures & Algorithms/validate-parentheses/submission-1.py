class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = { "(", "{", "["}

        for bracket in s:
            if bracket in opens:
                stack.append(bracket)
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