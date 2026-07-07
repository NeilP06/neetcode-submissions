class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        lefts = [0] * len(height)
        rights = [0] * len(height)

        for i in range(len(height)):
            if len(stack) == 0 or height[stack[-1]] > height[i]:
                stack.append(i)
                continue
            
            while len(stack) != 0 and height[stack[-1]] <= height[i]:
                index = stack.pop()
                rights[index] = i
            stack.append(i)

        while len(stack) != 0:
            index = stack.pop()
            rights[index] = 0

        for i in range(len(height) - 1, -1, -1):
            if len(stack) == 0 or height[stack[-1]] > height[i]:
                stack.append(i)
                continue
            
            while len(stack) != 0 and height[stack[-1]] <= height[i]:
                index = stack.pop()
                lefts[index] = i
            stack.append(i)

        while len(stack) != 0:
            index = stack.pop()
            lefts[index] = 0

        for i in range(len(height)):
            height_res = max(0, min(height[lefts[i]], height[rights[i]]) - height[i])
            print(height_res)
            result += height_res


        print(lefts, rights)
        return result