class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        start = 0
        match = 0
        if l2 < l1:
            return False
        char_table1 = [0] * 26
        char_table2 = [0] * 26

        for i in range(l1):
            char_table1[ord(s1[i]) - ord("a")] += 1
            char_table2[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            match += 1 if char_table1[i] == char_table2[i] else 0

        for i in range(l1, l2):
            if match == 26:
                return True
            curr_char_index = ord(s2[i]) - ord("a")
            start_char_index = ord(s2[start]) - ord("a")
            # right side
            char_table2[curr_char_index] += 1
            if char_table2[curr_char_index] == char_table1[curr_char_index]:
                match += 1
            elif char_table2[curr_char_index] == char_table1[curr_char_index] + 1:
                match -= 1
            # left side
            char_table2[start_char_index] -= 1
            if char_table2[start_char_index] == char_table1[start_char_index]:
                match += 1
            elif char_table2[start_char_index] == char_table1[start_char_index] - 1:
                match -= 1
            # update start index
            start += 1
        return match == 26
