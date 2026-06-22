# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.answer = 0
        self.traversed = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inOrder(root, k)
        return self.answer
    def inOrder(self, root: Optional[TreeNode], k: int):
        if root == None:
            return 
        self.inOrder(root.left, k)
        self.traversed += 1
        if self.traversed == k:
            self.answer = root.val
            return
        self.inOrder(root.right, k)

        