class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        hashset ={}
        for i in range(len(nums)):
            if nums[i] in hashset and abs(i - hashset[nums[i]]) <= k:
                return True
            hashset[nums[i]] = i
        return False
sol = Solution()
print(sol.containsNearbyDuplicate(nums=[1,2,3,1], k=3)) 