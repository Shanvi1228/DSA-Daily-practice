#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#By brute Force Method

class Solution(object):
    def twoSum(self, nums, target):
      for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (i==j):
                continue
            if(nums[i]+nums[j]==target):
                return i, j
#TestCase1
# nums = [2,7,11,15], 
# target = 9
# Output- [0,1]

#Time Complexity- O(N^2)
#Space Complexity- O(1)

#------------------------------------------------

