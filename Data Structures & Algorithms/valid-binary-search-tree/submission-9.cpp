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
    bool isValidBST(TreeNode* root) {
        return isGood(root, -1001, 1001);
    }
    bool isGood(TreeNode* root, int minVal, int maxVal) {
        if (!root) {
            return true;
        }
        if (root->val <= minVal or root->val >= maxVal) {
            return false;
        }
        return isGood(root->left, minVal, root->val) and isGood(root->right, root->val, maxVal);
    }
};
