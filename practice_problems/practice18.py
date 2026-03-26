def twoSum(nums, target):
    num_container = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_container:
            return(num_container[complement], index)
        num_container[num] = index
    return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
