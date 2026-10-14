class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        minS = 0
        for i in range(len(strs)):
            if len(strs[i]) < len(strs[minS]):
                minS = i
        for i in range(len(strs[minS])):
            ch = strs[minS][i]
            for s in strs:
                if s[i] != ch:
                    return ''.join(prefix)
            prefix.append(ch)
        return ''.join(prefix)
        
        


