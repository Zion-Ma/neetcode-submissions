# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.p = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(s: int, e: int):
            if s > e:
                return None
            curr = TreeNode(val = preorder[self.p])
            self.p += 1
            if s == e:
                return curr
            idx = inorder.index(curr.val)
            curr.left = helper(s, idx - 1)
            curr.right = helper(idx + 1, e)
            return curr
        return helper(0, len(preorder) - 1)

        