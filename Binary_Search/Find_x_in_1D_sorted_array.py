""" 
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
"""
class Solution(object):
    def search(self, nums, target):
     low = 0
     high = len(nums)-1
     while low <= high:
        mid = ( low + high )// 2
        if(nums[mid]==target):
            return mid
        elif (target > nums[mid]):
            low = mid + 1
        else:
            high = mid - 1
     return -1
      
  # Time Complexity- O(log n)
  # Space Complexity- O(1)
