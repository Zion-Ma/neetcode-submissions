class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        # n
        for s in strs:
            # O(slogs)
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        # time complexity: nslogs
        # space complexity: n
        res = [v for k, v in groups.items()]
        return res
