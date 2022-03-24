import math
class Solution(object):
    def product(self, numbers):
        res = 1
        for num in numbers:
            res = res * num
        return res

    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     zero_locations = [ix for ix, n in enumerate(nums) if not n]
    #     result = []
    #     prod = 0
    #     for i in range(len(nums)):
    #         if i > 0:
    #             # sublist = nums[0 : i] + nums[i+1 : len(nums)]
    #             if prod == 0:
    #                 sublist = nums[0 : i] + nums[i+1 : len(nums)]
    #                 prod = self.product(sublist)
    #             else:
    #                 prod = prod * nums[i-1]
    #                 # print(prod)

    #                 sum, count = abs(prod), 0
    #                 while sum > 0:
    #                     sum -= abs(nums[i])
    #                     count += 1
                    
    #                 if (prod < 0 and nums[i] < 0) or (prod > 0 and nums[i] > 0):
    #                     prod = count
    #                 else:
    #                     prod = count * -1
    #         else:
    #             sublist = nums[i+1 : len(nums)]
    #             prod = self.product(sublist)

    #         # print(sublist)
    #         result.append(prod)
    
    #     return result


    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_locations = [ix for ix, n in enumerate(nums) if not n]
        if len(zero_locations) > 1:
            return [0] * len(nums)
        elif len(zero_locations) == 1:
            result = [0] * len(nums)
            iz = zero_locations[0]
            sublist = nums[iz+1 : len(nums)]
            sublist.extend(nums[0 : iz]) if iz > 0 else None
            result[iz] = self.product(sublist)
            return result
        
        result = []
        full = self.product(nums)
        for n in nums:            
            # sum, count = abs(full), 0
            # print(">>>>>>>>>>>>>> n, SUM <<<<<<<<<<<<<<<<")
            # print(n, sum)
            # while sum > 0:
            #     # print(sum)
            #     sum -= abs(n)
            #     count += 1
            # print("--------------- DONE -----------------", '\n')
            # if (full < 0 and n < 0) or (full > 0 and n > 0):
            #     result.append(count)
            # else:
            #     result.append(count * -1)
            result.append(full//n)
    
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, -3, 4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    print(sol.productExceptSelf([5,9,2,-9,-9,-7,-8,7,-9,10]))

