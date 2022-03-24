class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max = 0
        local_sum = 0
        subseq = nums[0:k]
        for i in range(k):
            local_sum += nums[i]
        max = local_sum

        for i in range(k, len(nums)):
            local_sum = max + nums[i]
            del_j = -1
            for j, n in enumerate(subseq):
                if local_sum-n > max:
                    max = local_sum-n
                    del_j = j

            if del_j >= 0:
                del subseq[del_j]
                subseq.append(nums[i])
        
        return subseq

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubsequence([3,4,3,3], 2))
    print(sol.maxSubsequence([-1,-2,3,4], 3))
    print(sol.maxSubsequence([2,1,3,3], 2))