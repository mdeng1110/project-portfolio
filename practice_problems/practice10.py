from collections import Counter
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# print(x)


def twoSum(nums, target):
    #dictionary method
    num_container = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_container:
            return ([num_container[complement], index])
        num_container[num] = index
    return []
    #brute force method
    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []

def isAnagram(s, t):
    s = list(s)
    s = sorted(s)
    t = list(t)
    t = sorted(t)
    if s == t:
        return True
    return False
    
def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict

# nums = [2,7,11,15]
# target = 9
# print(twoSum(nums, target))

s = "anagram"
t = "nagaram"
print("Result of isAnagram: ", isAnagram(s, t))
print("Result of isAnagram2: ", isAnagram2(s, t))