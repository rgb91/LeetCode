# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# class Solution:
#     def inorderTraversal(self, root):
#         res = []
#         if root:
#             res = self.inorderTraversal(root.left) 
#             print(root.val, end=',')
#             res.append(root.val)
#             res = res + self.inorderTraversal(root.right)
#         return res
        
#     def setParentForNodes(self, root, parent):
#         if not root:
#             return True
        
#         root.parent = parent
        
#         return self.setParentForNodes(root.left, root) \
#             and self.setParentForNodes(root.right, root)
    
#     def distributeCoins(self, root: Optional[TreeNode]) -> int:
#         def pathprint(path):
#             print('Path: ', end='')
#             for node in path:
#                 print(node.val, '-> ', end='')
#             print()
        
#         def treeprint(root):
#             print('\t>> TREE: ', end='')
#             qu = [root]
#             while qu:
#                 node = qu.pop(0)
#                 print(f'{node.val}', end=',')
#                 if node.left: qu.append(node.left)
#                 if node.right: qu.append(node.right)
#             print()
            
#         def distributionHelper(root: Optional[TreeNode], steps: int, caller: Optional[TreeNode], zerocount: int):
#             if not root:
#                 return False, None, steps, zerocount
            
#             # print(f'\t>> Call: node={root.val} {steps=} {zerocount=}')

#             if root.val > 1: return True, root, steps, zerocount
            
#             iszero = 0
#             if root.val == 0: iszero = 1
            
#             minsteps = 102
#             donor = None
#             minzeros = 102
#             if root.left != caller:
#                 retl, donorl, stepsl, zerol = distributionHelper(root.left, steps+1, root, zerocount+iszero)
#                 if retl and stepsl <= minsteps and zerol < minzeros: minsteps, donor, minzeros = stepsl, donorl, zerol
#             if root.right != caller:
#                 retr, donorr, stepsr, zeror = distributionHelper(root.right, steps+1, root, zerocount+iszero)
#                 if retr and stepsr <= minsteps and zeror < minzeros: minsteps, donor, minzeros = stepsr, donorr, zeror
#             if root.parent != caller:
#                 retp, donorp, stepsp, zerop = distributionHelper(root.parent, steps+1, root, zerocount+iszero)
#                 if retp and stepsp <= minsteps and zerop < minzeros: minsteps, donor, minzeros = stepsp, donorp, zerop
                
#             if donor:
#                 return True, donor, minsteps, minzeros

#             return False, None, -1, zerocount
        
#         self.setParentForNodes(root, None)
        
#         totalsteps = 0
#         q = [root]
#         while q:
#             node = q.pop(0)
#             print('>> CALL:', node.val)
#             if node.val == 0:
#                 path = []
#                 ret, donor, steps, zerocount = distributionHelper(node, 0, node, 0)
#                 print(f'\t>> Current call output: {donor.val=}, {steps=}, {zerocount=}')
#                 donor.val -= 1
#                 node.val += 1
#                 treeprint(root)  # print tree

#                 totalsteps += steps
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
        
#         return totalsteps



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def setParentForNodes(self, root, parent):
        if not root:
            return True

        root.parent = parent

        return self.setParentForNodes(root.left, root) \
            and self.setParentForNodes(root.right, root)
    
    def pathprint(self, path, title='Path'):
        print(f'\t>> {title}: ', end='')
        for node in path:
            print(node.val, end=',')
        print()
    
    def treeprint(self, root):
        print('\t>> TREE: ', end='')
        qu = [root]
        while qu:
            node = qu.pop(0)
            print(f'{node.val}', end=',')
            if node.left: qu.append(node.left)
            if node.right: qu.append(node.right)
        print()
        
    def findNearestZeroNode(self, root: Optional[TreeNode], dist: int, caller: Optional[TreeNode]):
        if not root:
            return False, [None], -1
        
        # print(f'\t>> Call: node={root.val} {dist=}')
        
        if root.val == 0:  # success
            return True, [root], dist
        
        receivers, mindist = [], 111  # max 100 nodes, max 100 height/dist
        if root.left != caller:
            retl, recvrl, distl = self.findNearestZeroNode(root.left, dist+1, root)
            if retl and distl <= mindist: 
                mindist = distl
                receivers.append(recvrl[0])
        if root.right != caller:
            retr, recvrr, distr = self.findNearestZeroNode(root.right, dist+1, root)
            if retr and distr <= mindist: 
                mindist = distr
                receivers.append(recvrr[0])
        if root.parent != caller:
            retp, recvrp, distp = self.findNearestZeroNode(root.parent, dist+1, root)
            if retp and distp <= mindist: 
                mindist = distp
                receivers.append(recvrp[0])
        
        if receivers:
            return True, receivers, mindist
        
        return False, [None], -1
    
    def distribute(self, rnodes, dist, coinstodistribute, steps=0):
        each = coinstodistribute // len(rnodes)
        remainder = coinstodistribute % len(rnodes)
        for rcvnode in rnodes:
            rcvnode.val += each
            steps += (dist*each)
        for i in range(remainder):
            rnodes[i].val += 1
            steps += (dist*1)
        return steps
    
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.setParentForNodes(root, None)
        
        donorslist = []
        q = [root]
        while q:
            node = q.pop(0)
            if node.val > 1: donorslist.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        donorslist = sorted(donorslist, key=lambda node: node.val, reverse=True)        
        totalsteps = 0
        while donorslist:  # dnode = donor node, rnode = receiver node (zero and nearest)
            dnode = donorslist.pop(0)
            
            print('>> RUN:', dnode.val)
            coinstodistribute = dnode.val-1
            _, rnodes, distance = self.findNearestZeroNode(dnode, 0, dnode)
            totalsteps += self.distribute(rnodes, distance, coinstodistribute)
            dnode.val = 1
            
            for rnode in rnodes:
                if rnode.val > 1: 
                    donorslist.append(rnode)
            donorslist = sorted(donorslist, key=lambda node: node.val, reverse=True)
            
            self.pathprint(donorslist, 'Donors List')
            self.treeprint(root)

        return totalsteps