# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(curr) -> int:
            if curr is None:
                return 0
            left, right = dfs(curr.left), dfs(curr.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.ans
            
