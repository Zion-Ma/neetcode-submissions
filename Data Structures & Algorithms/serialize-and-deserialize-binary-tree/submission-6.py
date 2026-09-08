# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = list()
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                ser.append("N#")
            else:
                ser.append(str(node.val) + "#")
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return "".join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("#")
        self.i = 0
        def dfs() -> Optional[TreeNode]:
            # if self.i >= len(data):
            #     return None
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root

