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

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def threeSum(nums):
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        lo, hi = i+1, n-1
        while lo < hi:
            summ= nums[i] + nums[lo] + nums[hi]
            if summ == 0:
                answer.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo+1, hi-1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]:
                    hi -= 1
            elif summ < 0:
                lo += 1
            else:
                hi -= 1
    return answer 


# nums = [2,7,11,15]
# target = 9
# print(twoSum(nums, target))

# nums1 = [2,3,-2,4]
# print(maxProduct(nums1))

# print(factorial(4))

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))