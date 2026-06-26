class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minimums) == 0 or val < self.minimums[-1]:
            self.minimums.append(val)
        else:
            self.minimums.append(self.minimums[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        
