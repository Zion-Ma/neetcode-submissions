# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = [(root, -101)]
        good = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr[0].val >= curr[1]:
                    good += 1
                max_val = max(curr[1], curr[0].val)
                if curr[0].left:
                    queue.append((curr[0].left, max_val))
                if curr[0].right:
                    queue.append((curr[0].right, max_val))
        return good