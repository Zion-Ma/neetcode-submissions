# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, mini, maxi) -> True:
            if curr is None:
                return True
            if curr.val <= mini or curr.val >= maxi:
                return False
            return dfs(curr.left, mini, curr.val) and dfs(curr.right, curr.val, maxi)
        return dfs(root, -1001, 1001)
        
        