class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_range = 0
        for i in range(len(nums)):
            mn = nums[i]
            mx = nums[i]
            for j in range(i+1, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                total_range += (mx-mn)
        
        return total_range

if __name__ == '__main__':
    sol = Solution()
    # print(sol.subArrayRanges([1, 2, 3]))
    print(sol.subArrayRanges([4,-2,-3,4,1]))