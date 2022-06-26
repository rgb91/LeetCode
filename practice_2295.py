# nums = [1,2,4,6]
# operations = [[6,1],[4,7], [1,3]]
# nums = [1,2]
# operations = [[1,3],[2,1],[3,2]]
# nums = [10]
# operations = [[10,9],[9,8],[8,7],[7,5]]
nums = [1,2,3]
operations = [[1,10],[10,100],[3,99]]


def binary_search(numbers, target):
    l, r = 0, len(numbers)-1
    while l <= r:
        mid = l + (r - l) // 2
        if numbers[mid][0] == target: return mid
        elif numbers[mid][0] < target: l = mid + 1
        else: r = mid - 1
    return -1


def search_insert_index(numbers, target):    
    l , r = 0, len(numbers)-1
    while l <= r:
        mid = (l + r) // 2
        if numbers[mid][0] == target: return mid
        elif numbers[mid][0] < target: l = mid + 1
        else: r = mid - 1
    return l


nums = [[n, i] for i, n in enumerate(nums)]  # to memorize original index
nums = sorted(nums)

n, m = len(nums), len(operations)
for old, new in operations:
    i = binary_search(nums, old)
    t_pos = nums[i][1]
    del nums[i:i+1]
    k = search_insert_index(nums, new)
    nums[k:k] = [[new, t_pos]]
ret_nums = [-1]*n
for num, ix in nums:
    ret_nums[ix] = num
print(ret_nums)