# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, height=-1, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = height
        self.parent = parent
        
class Solution:
    def setHeightAndParentForNodes(self, root, parent, parent_height, height_map):
        if not root:
            return True
        root.height = parent_height + 1
        root.parent = parent
        if root.height not in height_map: height_map[root.height] = [root]
        else:
            height_map[root.height].append(root)
        return self.setHeightAndParentForNodes(root.left, root, root.height, height_map) \
            and self.setHeightAndParentForNodes(root.right, root, root.height, height_map)
    
    def getPathFromRoot(self, root, node, path):
        if not root: return False
        
        path.append(root)
        if root.val == node.val: return True
        
        if self.getPathFromRoot(root.left, node, path) or self.getPathFromRoot(root.right, node, path):
            return True
        
        path.pop()
        return False
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        hmap = {}
        self.setHeightAndParentForNodes(root, None, -1, hmap)
        maxh = max(hmap)
        
        if len(hmap[maxh]) == 1: return hmap[maxh][0]
        
        paths = {node.val: [] for node in hmap[maxh]}
        for node in hmap[maxh]: self.getPathFromRoot(root, node, paths[node.val])
        
        i, found = 0, False
        refnode = hmap[maxh][0]
        while i <= maxh:
            checkval = paths[refnode.val][i].val
            for val, path in paths.items():
                if path[i].val != checkval:
                    found = True
                    break
            if found: break
            i += 1
        return paths[refnode.val][i-1]
