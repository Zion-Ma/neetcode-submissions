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
    int idx;
    unordered_map<int, int> pos;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        idx = 0;
        for (int i = 0; i < inorder.size(); i++) {
            pos[inorder[i]] = i;
        }
        TreeNode* root = buildNode(0, (int)inorder.size() - 1, preorder, inorder);
        return root;
    }
    TreeNode* buildNode(int left, int right, vector<int>& preorder, vector<int>& inorder) {
        if (left > right) {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[idx]);
        int inorder_pos = pos[preorder[idx]];
        idx++;
        root->left = buildNode(left, inorder_pos - 1, preorder, inorder);
        root->right = buildNode(inorder_pos + 1, right, preorder, inorder);
        return root;
    }
};
