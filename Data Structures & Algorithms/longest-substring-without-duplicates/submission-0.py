class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        char_set = set()
        max_len = 0
        for i in range(len(s)):
            if s[i] not in char_set:
                char_set.add(s[i])
                max_len = max(max_len, i - l + 1)
            else:
                while(s[i] in char_set):
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[i])
        return max_len
            


        
        