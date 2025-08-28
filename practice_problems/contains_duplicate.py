class Solution:
    def containsDuplicate(nums):
        dictionary = {}
        for i in range(len(nums)):
           if nums[i] not in dictionary:
                dictionary[nums[i]] = 1
           else:
                dictionary[nums[i]] += 1
        for value in dictionary:
            if dictionary[value] > 1:
                return True
        return False
    
nums = [1,2,3,1]
            
print(Solution.containsDuplicate(nums))