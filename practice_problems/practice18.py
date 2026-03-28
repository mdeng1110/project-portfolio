def twoSum(nums, target):
    num_container = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_container:
            return(num_container[complement], index)
        num_container[num] = index
    return []


def maxProduct(nums1):
    cur_max = cur_min = ans = nums1[0]
    for x in nums1[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max*x)
        cur_min = min(x, cur_min*x)
        ans = max(ans, cur_max)
    return ans

nums = [2,7,11,15]
target = 9
# print(twoSum(nums, target))

nums1 = [2,3,-2,4]
print(maxProduct(nums1))
