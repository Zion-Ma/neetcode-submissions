class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool wordEnd;
    TrieNode() {wordEnd = false;}
    void addWord(const string& s) {
        TrieNode* curr = this;
        for (char c : s) {
            if (!curr->children.count(c)) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->wordEnd = true;
    }
};

class Solution {
public:
    vector<string> result;
    TrieNode* root;
    vector<vector<bool>> seen;
    int m, n;
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        m = (int)board.size();
        n = (int)board[0].size();
        seen.assign(m, vector<bool>(n, false));
        root = new TrieNode();
        for (const string& s : words) {
            root->addWord(s);
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                TrieNode* curr = root;
                string word = "";
                backtrack(r, c, board, curr, word);
            }
        }
        return result;
    }
    void backtrack(int r, int c, const vector<vector<char>>& board, TrieNode* curr, string word) {
        if (
            r >= m or r < 0 or
            c >= n or c < 0 or
            seen[r][c] or !curr->children.count(board[r][c])
        ) {return;}
        TrieNode* parent = curr;
        char ch = board[r][c];
        curr = curr->children[ch];
        seen[r][c] = true;
        if (curr->wordEnd){result.push_back(word + ch);}
        curr->wordEnd = false;
        backtrack(r + 1, c, board, curr, word + ch);
        backtrack(r - 1, c, board, curr, word + ch);
        backtrack(r, c + 1, board, curr, word + ch);
        backtrack(r, c - 1, board, curr, word + ch);
        seen[r][c] = false;
        if (curr->children.empty()) {
            parent->children.erase(ch);
            delete curr;
        }
    }
};
