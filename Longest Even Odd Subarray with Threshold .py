class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        ans = 0
        l = 0
        n = len(nums)
        
        while l < n:
            # 1. Condition: Subarray must start with an even number <= threshold
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l + 1
                # 2. Condition: Extend while alternating parity and within threshold
                while r < n and nums[r] % 2 != nums[r-1] % 2 and nums[r] <= threshold:
                    r += 1
                
                # Update the maximum length found
                ans = max(ans, r - l)
                
                # Move 'l' to 'r' to start checking the next potential subarray
                # Because if a subarray ends at r-1, the next possible start 
                # is r or later.
                l = r 
            else:
                # If current index doesn't start with even/valid num, move to next
                l += 1
                
        return ans
