""" 
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array.
"""

class Solution:
    def lowerBound(self, nums, x):
        low = 0
        high = len(nums)-1
        ans = len(nums)
        while (low <= high):
            mid = ( low + high )// 2
            if(nums[mid] >= x):
                high = mid - 1
                ans = mid
            else :
                low = mid + 1
        return ans

# Time Complexity- O(log n)
# Space Complexity- O(1)
        
