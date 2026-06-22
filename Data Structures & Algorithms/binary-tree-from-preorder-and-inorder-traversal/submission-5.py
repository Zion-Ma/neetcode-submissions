# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v:i for i, v in enumerate(inorder)}
        self.i = 0
        def dfs(l: int, r: int) -> TreeNode:
            if l > r:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = dfs(l, index_map[root.val] - 1)
            root.right = dfs(index_map[root.val] + 1, r)
            return root
        return dfs(0, len(preorder) - 1)
