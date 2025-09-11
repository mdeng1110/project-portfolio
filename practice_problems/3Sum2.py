def threeSum(nums):
    #sort list
    nums.sort()
    #create result list
    res = []

    for i in range(len(nums)):
        #skip duplicate first nums
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums)-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            print('TOTAL: ', total)
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                #skip the duplicate 2nd and 3rd numbers
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))