class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def traverse(currList: list, currSum: int, i: int) -> None:
            if currSum == target:
                result.append(currList.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            if currSum + candidates[i] <= target:
                currList.append(candidates[i])
                traverse(currList, currSum + candidates[i], i + 1)
                currList.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            traverse(currList, currSum, i + 1)
        traverse([], 0, 0)
        return result
