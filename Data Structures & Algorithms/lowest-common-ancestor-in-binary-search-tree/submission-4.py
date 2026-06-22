# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxi, mini = max(p.val, q.val), min(p.val, q.val)
        while root:
            if root.val > maxi:
                root = root.left
            elif root.val < mini:
                root = root.right
            else:
                return root
        