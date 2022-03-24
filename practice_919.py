# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.current = root

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        q = [self.root]
        while q:
            currnode = q.pop(0)
            if not currnode.left:
                currnode.left = node
                return currnode.val
            if not currnode.right:
                currnode.right = node
                return currnode.val
            q.append(currnode.left)
            q.append(currnode.right)
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()