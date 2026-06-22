class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(s)
        return list(word_dict.values())