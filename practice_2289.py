class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [[nums[0], 0]]  # num, steps
        res = 0

        for n in nums[1:]:
            step = 0
            while stack and n >= stack[-1][0]:
                step = max(stack.pop()[1], step)
            step = step + 1 if stack else 0
            stack.append([n, step])
            res = max(res, step)
        return res

# nums = [5,1,2,3,1,2,4]
# # nums = [5,6,7,8]

# stack = [[nums[0], 0]]  # num, steps
# res = 0

# for n in nums[1:]:
#     # print(nums)
#     # print(f'{n=}')
#     step = 0
#     while stack and n >= stack[-1][0]:
#         # print(f'pop={stack[-1][0]}, {step=}, {stack[-1][1]}')
#         step = max(stack.pop()[1], step)
#     step = step + 1 if stack else 0  # calculate step count or reset if empty stack
#     stack.append([n, step])
#     # print(stack)
#     # print(f'{step=}')
#     # print()
#     res = max(res, step)

# print(res)







# # stack, ans = [[0, nums[0]]], 0
# # for n in nums[1:]:
# #     step = 0
# #     while stack and stack[-1][1] <= n:
# #         step = max(step, stack[-1][0])
# #         stack.pop()
# #     step = step+1 if stack else 0
        
# #     stack.append([step, n])
# #     print(stack)
# #     ans = max(ans, step)