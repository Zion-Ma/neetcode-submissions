class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = temperatures.__len__()
        stack = [0]
        output = [0] * n
        for i in range(1, n):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                output[last] = i - last
            stack.append(i)
        return output
            
