class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            # print(f"{t}:{stack}")
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop() 
                result[j] = i - j
            stack.append(i)
        return result
