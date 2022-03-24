# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getNodeGivenValue(self, root, value):
        if not root:  # None
            return False

        if root.val == value:  # Found
            return root
        
        left = self.getNodeGivenValue(root.left, value)
        if left is not None:
            return left
        
        right = self.getNodeGivenValue(root.right, value)
        return right


    def getPathFromRoot(self, root, value, path):
        
        if not root:  # None
            return False

        path.append(root.val)
        if root.val == value:  # Found
            return True
        
        if self.getPathFromRoot(root.left, value, path) or self.getPathFromRoot(root.right, value, path):
            return True
        
        path.pop()
        return False

    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        start_node_path = []
        self.getPathFromRoot(root, startValue, start_node_path)
        dest_node_path = []
        self.getPathFromRoot(root, destValue, dest_node_path)

        # print(start_node_path)
        # print('')
        # print(dest_node_path)

        i, j = 0, 0
        intersection = -1
        start_to_up = 0
        result = ''
        while i < len(start_node_path) or j < len(dest_node_path):
            if i == j and start_node_path[i] == dest_node_path[j]:
                i += 1
                j += 1
            else:
                intersection = j - 1
                start_to_up = len(start_node_path) - i
                result = ''.join('U' for temp in range(start_to_up))
                break
        
        intersection_node = self.getNodeGivenValue(dest_node_path[intersection])
        for ix in range(intersection+1, len(dest_node_path)):
            if dest_node_path[ix] == intersection_node.left.val:
                result += 'L'
            else:
                result += 'R'
            
        return result

# [1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]
# 6
# 15