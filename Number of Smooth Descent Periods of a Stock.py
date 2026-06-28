class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        # Each single element is a smooth descent period of length 1
        total_periods = 1
        # 'current_streak' tracks periods ending at the previous index
        current_streak = 1
        
        for i in range(1, len(prices)):
            # If the price decreases by exactly 1, the streak continues
            if prices[i] == prices[i - 1] - 1:
                current_streak += 1
            else:
                # Streak resets to 1 (the single element at i)
                current_streak = 1
            
            # The number of smooth descent periods ending at i is exactly current_streak
            total_periods += current_streak
            
        return total_periods
