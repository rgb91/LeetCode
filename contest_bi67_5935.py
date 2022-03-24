class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        dec_count, inc_count = 0, 0
        dec_list, inc_list = [0]*len(security), [0]*len(security)
        for i in range(1, len(security)):
            dec_count = dec_count + 1 if security[i] <= security[i-1] else 0
            dec_list[i] = dec_count
        for i in range(len(security)-2, -1, -1):
            inc_count = inc_count + 1 if security[i] <= security[i+1] else 0
            inc_list[i] = inc_count

        result = []
        for i, (dec, inc) in enumerate(zip(dec_list, inc_list)):
            if dec >= time and inc >= time:
                result.append(i)
        
        return result

        # order_sum = [order[0]]
        # for i in range(1, time):
        #     order_sum[i] = order_sum[i-1] + order[i]

        # for i in range(time, len(security)):
        #     order_sum = order_sum[i-1] + order[i] - order[i-time]
        #     if order_sum == 0 or order_sum

        # result = []
        # for i in range(time, len(order)-time):
        #     left = order[i-time:i]
        #     right = order[i+1:i+time+1]

        #     for 


if __name__ == '__main__':
    sol = Solution()
    # print(sol.goodDaysToRobBank([5,3,3,3,5,6,2], 2))
    # print(sol.goodDaysToRobBank([1,1,1,1,1], 0))
    # print(sol.goodDaysToRobBank([1,2,3,4,5,6], 1))
    # print(sol.goodDaysToRobBank([1], 5))

    print(sol.goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], 2))  # [5,10,14]