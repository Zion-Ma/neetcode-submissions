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

class Solution {
public:
    int curr_idx = 0;
    // unordered_set<int> seen;
    unordered_map<int, int> pos;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = (int)inorder.size();
        for (int i = 0; i < n; i++) {
            pos[inorder[i]] = i;
        }
        TreeNode* root = buildNode(0, n - 1, preorder, inorder);
        return root;
    }
    TreeNode* buildNode(
        int left, int right, 
        vector<int>& preorder, vector<int>& inorder
    ) {
        if (left > right) {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[curr_idx]);
        int inorder_pos = pos[preorder[curr_idx]];
        curr_idx++;
        root->left = buildNode(left, inorder_pos - 1, preorder, inorder);
        root->right = buildNode(inorder_pos + 1, right, preorder, inorder);
        return root;
    }
};
