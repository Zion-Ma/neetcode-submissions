class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = (int)s.size() - 1;
        while (left < right) {
            while (left < right and !alphaNum(s[left])) left++;
            while (left < right and !alphaNum(s[right])) right--;
            if (tolower(s[left]) != tolower(s[right])) return false;
            left++;
            right--;
        }
        return true;
    }

    bool alphaNum(char c) {
        return std::isalpha(c) or std::isdigit(c);
    }
};
