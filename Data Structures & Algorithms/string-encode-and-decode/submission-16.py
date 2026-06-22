class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += s[::-1] + "/t"
        return enc

    def decode(self, s: str) -> List[str]:
        ori = s.split("/t")
        for i, word in enumerate(ori):
            ori[i] = word[::-1]
        return ori[:-1]

