# [[1,5,9],[10,11,13],[12,13,15]]
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        mlist = []
        for line in matrix:
            for item in line:
                mlist.append(item)
        
        mlist = sorted(mlist)
        return mlist[k-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))