# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, mini, maxi):
            if root is None:
                return True
            elif mini >= root.val or maxi <= root.val:
                return False
            else:
                return valid(root.left, mini, root.val) and valid(root.right, root.val, maxi)
        if root is None:
            return False
        else:
            return valid(root, float("-inf"), float("inf"))
        