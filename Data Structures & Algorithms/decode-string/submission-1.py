class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i: int) -> tuple[str, int]:
            res = []
            k = 0
            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                    continue
                if s[i] == '[':
                    recur_str, last_i = decode(i + 1)
                    res.append(recur_str * k)
                    k = 0
                    i = last_i + 1
                else:
                    res.append(s[i])
                    i += 1
            return (''.join(res), i)
        return decode(0)[0]