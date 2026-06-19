class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        best = 0
        
        while left < right:
            best = max(best, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return best
