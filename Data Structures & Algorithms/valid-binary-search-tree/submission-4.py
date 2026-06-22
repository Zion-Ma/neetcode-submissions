# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, -1001, 1001)]
        while queue:
            curr, mini, maxi = queue.pop(0)
            if not(mini < curr.val < maxi):
                return False
            if curr.left:
                queue.append((curr.left, mini, curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, maxi))
        return True