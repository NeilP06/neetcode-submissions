class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Makes casing much more convenient
        operators = { "+", "-", "*", "/"}
        stack = []

        # Iterate through the tokens, O(n) work
        for token in tokens:
            # Add numbers only to the stack, O(1) work
            if token not in operators:
                stack.append(int(token))
                continue

            # Get top two numbers from stack in case of operator, O(1) work
            second : int = stack.pop()
            first : int = stack.pop()

            # Perform valid operation and add to stack, O(1) work
            if token == "+":
                stack.append(first + second)
            elif token == "-":
                stack.append(first - second)
            elif token == "*":
                stack.append(first * second)
            else:
                # Round down towards 0
                result = int(first / second)
                stack.append(result)

        # Return the remaining result (last element of stack), O(1) work
        return stack.pop()