# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val:idx for idx, val in enumerate(inorder)}
        self.p = 0
        def dfs(s, e) -> TreeNode:
            if s > e:
                return None
            curr = TreeNode(val = preorder[self.p])
            self.p += 1
            if s == e:
                return curr
            idx = pos[curr.val]
            curr.left = dfs(s, idx - 1)
            curr.right = dfs(idx + 1, e)
            return curr
        return dfs(0, len(preorder) - 1)
        
        