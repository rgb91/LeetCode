# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def print_path(self, path):
        val_list = []
        for node in path:
            val_list.append(node.val)
        print(val_list)
        
    
    def getPathFromRoot(self, root, node, path):
        
        if not root:  # None
            return False

        path.append(root)
        if root.val == node.val:  # Found
            return True
        
        if self.getPathFromRoot(root.left, node, path) or self.getPathFromRoot(root.right, node, path):
            return True
        
        path.pop()
        return False
    

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        self.getPathFromRoot(root, p, p_path)
        # self.print_path(p_path)
        
        q_path = []
        self.getPathFromRoot(root, q, q_path)
        # self.print_path(q_path)
        
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i].val == q_path[i].val:
            i+=1
        print(i)
        return p_path[i-1]