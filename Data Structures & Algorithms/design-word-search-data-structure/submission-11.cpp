class Node {
public:
    unordered_map<char, Node*> children;
    bool word_end;
    Node() {
        word_end = false;
    }
};

class WordDictionary {
public:
    Node* root;
    WordDictionary() {
        root = new Node();
    }
    
    void addWord(string word) {
        Node* curr = root;
        for (char ch : word) {
            if (curr->children.find(ch) == curr->children.end()) {
                curr->children[ch] = new Node();
            }
            curr = curr->children[ch];
        }
        curr->word_end = true;
    }
    
    bool search(string word) {
        return sub_search(word, 0, root);
    }
    bool sub_search(const string& word, int idx, Node* curr_root) {
        if (idx == word.size()) {return curr_root->word_end;}
        if (word[idx] == '.') {
            for (const auto& [ch, node] : curr_root->children) {
                if (sub_search(word, idx + 1, node)) {
                    return true;
                }
            }
            return false;
        } else {
            if (curr_root->children.find(word[idx]) == curr_root->children.end()) {
                return false;
            }
            return sub_search(word, idx + 1, curr_root->children[word[idx]]);
        }
    }
};
