# Optimal Approach
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
          
            if nums[i] != 0 and nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
            
          if nums[j] != 0:
                j += 1

#Time Complexity: O(N)
#Space Complexity: O(1)
