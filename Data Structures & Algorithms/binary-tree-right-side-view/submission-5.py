# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(curr, depth):
            if curr is None:
                return
            if depth == len(ans):
                ans.append(curr.val)
            dfs(curr.right, depth + 1)
            dfs(curr.left, depth + 1)
        dfs(root, 0)
        return ans