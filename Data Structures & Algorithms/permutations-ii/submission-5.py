class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i: int, count: Counter, curr: list) -> None:
            if i == len(nums):
                res.append(curr.copy())
                return
            for num in count.keys():
                if count.get(num) == 0:
                    continue
                count[num] -= 1
                curr.append(num)
                backtrack(i + 1, count, curr)
                count[num] += 1
                curr.pop()
            return

        count = Counter(nums)
        res = []
        backtrack(0, count, [])
        return res

                    