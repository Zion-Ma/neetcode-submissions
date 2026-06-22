class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        leng = temperatures.__len__()
        stack = [leng - 1]
        res = [0] * leng
        for i in range(leng - 2, -1, -1):
            curr = temperatures[i]
            while stack and curr >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
                