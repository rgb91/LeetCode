class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 10**5
        res = 0
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            sub_target = target - nums[i]
            
            while l < r:
                local_sum = nums[l] + nums[r]
                diff = abs(local_sum - sub_target)
                if diff < min_diff:
                    min_diff = diff
                    res = local_sum + nums[i]
                if local_sum > sub_target:
                    r -= 1
                elif local_sum < sub_target:
                    l += 1
                else:
                    break
            
        return res