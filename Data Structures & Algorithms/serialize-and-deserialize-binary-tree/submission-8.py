# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node: TreeNode) -> None:
            if not node:
                ser.append("N#")
            else:
                ser.append(f"{node.val}#")
                dfs(node.left)
                dfs(node.right)
        ser = list()
        dfs(root)
        return ''.join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        des = data.split("#")
        def build() -> TreeNode:
            if des[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(eval(des[self.i]))
            self.i += 1
            node.left = build()
            node.right = build()
            return node
        root = build()
        return root

