class Solution(object):
    def checkPartition(self, start, matchsticks, used_matches, leftover_partition, curr_partition_sum, target_sum):
        if leftover_partition == 1:
            return True

        if curr_partition_sum == target_sum:
            return self.checkPartition(0, matchsticks, used_matches, leftover_partition-1, 0, target_sum)
        
        for i in range(start, len(matchsticks)):
            if not used_matches[i]:
                used_matches[i] = True
                # print(leftover_partition, i, used_matches)
                if self.checkPartition(i+1, matchsticks, used_matches, leftover_partition, curr_partition_sum + matchsticks[i], target_sum):
                    return True
                else:
                    used_matches[i] = False
        
        return False

    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        sum = 0
        for match in matchsticks:
            sum += match
        if sum % 4:
            return False
        # matchsticks = sorted(matchsticks)
        required_match_length = sum // 4
        if any(i > required_match_length for i in matchsticks):
            return False
        
        used_matches = [False]*len(matchsticks)
        return self.checkPartition(0, matchsticks, used_matches, 4, 0, required_match_length)
        

if __name__ == '__main__':
    sol = Solution()
    # print(sol.makesquare([1,1,2,2,2]))
    # print(sol.makesquare([3,3,3,3,4]))
    print(sol.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
