class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += (s[::-1] + "\t")
        return enc
    def decode(self, s: str) -> List[str]:
        sep = s.split("\t")[:-1]
        return [word[::-1] for word in sep]
