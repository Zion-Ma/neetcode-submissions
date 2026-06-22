class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        records = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                records[j] = i - j
            stack.append(i)
        return records
