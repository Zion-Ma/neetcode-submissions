class Solution:
    def decodeString(self, s: str) -> str:
        def sub_string(i: int) -> tuple[str, int]:
            if i == len(s):
                return ("", i)
            sub_s = []
            digit = []
            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    digit.append(s[i])
                    i += 1
                    continue
                if len(digit) != 0:
                    recur_str, last_i = sub_string(i + 1)
                    count = int(''.join(digit))
                    sub_s += [recur_str for _ in range(count)]
                    digit = []
                    i = last_i + 1
                else:
                    sub_s.append(s[i])
                    i += 1
            return (''.join(sub_s), i)
        ans, _ = sub_string(0)
        return ans

                    