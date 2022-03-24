# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, height=-1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height
        
class Solution(object):

    def setHeightForNodes(self, root, parent_height, height_map):
        if not root:
            return True
        root.height = parent_height + 1
        if root.height not in height_map: height_map[root.height] = root.val
        else:
            height_map[root.height] = max(height_map[root.height], root.val)
        return self.setHeightForNodes(root.left, root.height, height_map) and self.setHeightForNodes(root.right, root.height, height_map)

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hmap = {}
        self.setHeightForNodes(root, -1, hmap)
        return hmap.values()