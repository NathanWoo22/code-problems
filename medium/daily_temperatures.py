class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0 or t <= stack[-1][0]:
                stack.append((t, i))
            
            else:
                while len(stack) > 0 and t > stack[-1][0]:
                    tmp = stack.pop()
                    output[tmp[1]] = i - tmp[1]
                stack.append((t, i))
        return output
