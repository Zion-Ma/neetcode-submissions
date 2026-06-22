from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            str_key = "".join(sorted(s))
            str_dict[str_key].append(s)
        return list(str_dict.values())

        