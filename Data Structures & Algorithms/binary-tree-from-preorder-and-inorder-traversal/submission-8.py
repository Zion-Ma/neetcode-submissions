# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        pos = dict()
        for i, n in enumerate(inorder):
            pos[n] = i
        def build(l: int, r: int) -> TreeNode:
            if l > r:
                return None
            curr = preorder[self.i]
            root = TreeNode(curr)
            self.i += 1
            idx = pos[curr]
            root.left = build(l, idx - 1)
            root.right = build(idx + 1, r)
            return root
        root = build(0, len(preorder) - 1)
        return root
            