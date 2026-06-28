class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 1. Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # 2. Slide the window across the array
        for i in range(k, len(nums)):
            # Subtract the element exiting the window and add the one entering
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            
        # 3. Return the maximum sum divided by k
        return max_sum / k
