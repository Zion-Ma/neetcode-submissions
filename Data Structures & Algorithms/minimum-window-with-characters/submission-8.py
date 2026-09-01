class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sl, tl = len(s), len(t)
        if sl < tl:
            return ""
        res_len = 100001
        countT, window = defaultdict(int), defaultdict(int)
        have, need = 0, 0
        left = 0
        res_start = 0
        for ch in t:
            countT[ch] += 1
        need = len(countT)
        for r in range(sl):
            ch = s[r]
            window[ch] += 1
            if (ch in countT and window[ch] == countT[ch]):
                have += 1
            while have == need:
                curr_len = r - left + 1
                if curr_len < res_len:
                    res_len = curr_len
                    res_start = left
                window[s[left]] -= 1
                if (s[left] in countT and window[s[left]] < countT[s[left]]):
                    have -= 1
                left += 1
        return "" if res_len == 100001 else s[res_start:res_start + res_len]
                