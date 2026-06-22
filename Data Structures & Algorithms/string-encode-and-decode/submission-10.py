class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += s[::-1]+"\t"
        return enc

    def decode(self, s: str) -> List[str]:
        strs = s.split("\t")[:-1]
        for i in range(len(strs)):
            strs[i] = strs[i][::-1]
        return strs