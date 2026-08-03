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
        return sub_search(word, root);
    }
    bool sub_search(string sub_word, Node* curr_root) {
        for (int i = 0; i < sub_word.size(); i++) {
            if (sub_word[i] == '.') {
                for (const auto& [ch, node] : curr_root->children) {
                    if (sub_search(sub_word.substr(i + 1), node)) {
                        return true;
                    }
                }
                return false;
            } else {
                if (curr_root->children.find(sub_word[i]) == curr_root->children.end()) {
                    return false;
                }
                curr_root = curr_root->children[sub_word[i]];
            }
        }
        return curr_root->word_end;
    }
};
