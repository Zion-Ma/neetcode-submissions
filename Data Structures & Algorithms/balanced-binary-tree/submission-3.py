# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr) -> tuple:
            if curr is None:
                return (True, 0)
            left = dfs(curr.left)
            right = dfs(curr.right)
            balanced = True
            if not left[0] or not right[0] or abs(left[1] - right[1]) > 1:
                balanced = False
            return (balanced, 1 + max(left[1], right[1]))
        return dfs(root)[0]
            
        