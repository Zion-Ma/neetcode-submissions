# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ser = ""
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                self.ser += "N"
                self.ser += "#"
            else:
                self.ser += str(node.val)
                self.ser += "#"
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.ser
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        def dfs() -> Optional[TreeNode]:
            if self.i >= len(data):
                return None
            start = self.i
            while self.i < len(data) and data[self.i] != "#":
                self.i += 1
            if data[start:self.i] == "N":
                self.i += 1
                return None
            else:
                node = TreeNode(int(data[start:self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()
                return node
        root = dfs()
        return root

