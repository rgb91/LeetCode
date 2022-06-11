from math import log2
nums = [1,3,5,2,4,8,2,2]

n = len(nums)
steps = int(log2(n))

for _ in range(steps):
    toggle, nums2 = True, []
    for i in range(0, len(nums)-1, 2):
        x = min(nums[i], nums[i+1]) if toggle else max(nums[i], nums[i+1])
        nums2.append(x)
        toggle = not toggle
    nums = nums2
print(nums[0])