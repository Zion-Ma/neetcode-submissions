/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Codec {
public:
    int i;
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s;
        dfs(root, s);
        string serial(s.begin(), s.end());
        return serial;
    }
    void dfs(TreeNode* root, string& s) {
        if (root == nullptr) {
            s += "N#";
            return;
        }
        s += to_string(root->val);
        s.push_back('#');
        dfs(root->left, s);
        dfs(root->right, s);
    }


    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        i = 0;
        vector<string> parsed = parse(data);
        TreeNode* root = build(parsed);
        return root;
    }
    vector<string> parse(string data) {
        int n = (int)data.size();
        int l = 0, r = 0;
        vector<string> parsed;
        while (r < n) {
            while (r < n and data[r] != '#') {
                r++;
            }
            parsed.push_back(data.substr(l, r - l));
            r++;
            l = r;
        }
        return parsed;
    }
    TreeNode* build(const vector<string>& parsed) {
        if (i >= (int)parsed.size() or parsed[i] == "N") {
            i++;
            return nullptr;
        }
        TreeNode* node = new TreeNode(stoi(parsed[i]));
        i++;
        node->left = build(parsed);
        node->right = build(parsed);
        return node;
    }
};
