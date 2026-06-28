from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # 1. Count the frequency of each number
        counts = Counter(nums)
        max_length = 0
        
        # 2. Iterate through the unique numbers in the map
        for x in counts:
            # Check if a pair exists (x, x+1)
            if x + 1 in counts:
                # Calculate length and update max_length
                max_length = max(max_length, counts[x] + counts[x + 1])
                
        return max_length
