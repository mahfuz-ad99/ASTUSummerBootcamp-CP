class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        # 1. Sort the array to easily access smallest and largest
        nums.sort()
        
        n = len(nums)
        max_sum = 0
        
        # 2. Use two pointers to pair smallest and largest
        left = 0
        right = n - 1
        
        while left < right:
            # Calculate sum of current pair
            current_sum = nums[left] + nums[right]
            
            # Keep track of the maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
            # Move pointers toward the center
            left += 1
            right -= 1
            
        return max_sum
