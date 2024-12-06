'''
Understand the problem:
Keypoints:
1. You can only hold at most one share of the stock at any time.
2. You can buy it and then immediately sell it on the same day.
3. Find the maximum profit we can achieve.
Possible solution: DP
- Use `dp` to track maximum profit for each day.
- dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
- Runtime: O(N), Space: O(N)
Solution: Greedy
- Greedy approach focuses on maximizing profit without tracking individual days.
- Runtime: O(N), Space: O(1)
Steps:
1. Traverse from day 1. If profit for the day is greater than 0, add it to `max_profit`.
2. If profit is 0 or negative, skip the day.
3. Return the cumulative profit.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit from buying and selling stocks multiple times.
        Args:
            prices (List[int]): List of stock prices where prices[i] is the price on the ith day.
        Returns:
            int: The maximum profit that can be achieved.
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] <= 0:
                continue
            max_profit += prices[i] - prices[i-1]
        return max_profit