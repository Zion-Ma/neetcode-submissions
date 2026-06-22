# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root) -> tuple:
            if root is None: return (True, 0)
            left, right = dfs(root.left), dfs(root.right)
            depth = 1 + max(left[1], right[1])
            if not left[0] or not right[0]:
                return (False, depth)
            balanced = (abs(left[1] - right[1]) <= 1)
            return (balanced, depth)
        return dfs(root)[0]