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
    int kth;
    int ans;
    int kthSmallest(TreeNode* root, int k) {
        kth = k;
        ans = 0;
        dfs(root);
        return ans;
    }
    void dfs(TreeNode* root) {
        if (!root) {
            return;
        }
        dfs(root->left);
        kth--;
        if (kth == 0) {
            ans = root->val;
            return;
        }
        dfs(root->right);
    }
};
