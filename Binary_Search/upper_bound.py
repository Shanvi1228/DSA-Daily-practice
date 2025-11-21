# Implement upper bound

class Solution:
    def upperBound(self, nums, x):
        low = 0
        high = len(nums)-1
        ans = len(nums)
        while (low <= high):
            mid = ( low + high )// 2
            if(nums[mid] > x):
                high = mid - 1
                ans = mid
            else :
                low = mid + 1
        return ans

# Time Complexity- O(log n)
# Space Complexity- O(1)
        
