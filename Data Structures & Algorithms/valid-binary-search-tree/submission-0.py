# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
    def valid(self, root: Optional[TreeNode], minimum: float, maximum: float) -> bool:
        if root == None:
            return True
        if minimum >= root.val or maximum <= root.val:
            return False
        return self.valid(root.left, minimum, root.val) and self.valid(root.right, root.val, maximum)
        
        