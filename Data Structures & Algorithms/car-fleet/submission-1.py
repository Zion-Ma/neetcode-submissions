class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = sorted([(idx, pos) for idx, pos in enumerate(position)], key = lambda x:x[1], reverse = True)
        stack = []
        for idx, pos in p:
            time = (target - pos) / speed[idx]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return stack.__len__()

        