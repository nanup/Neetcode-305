# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Example 1:
    # Input: prices = [7,1,5,3,6,4]
    # Output: 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Example 2:
    # Input: prices = [7,6,4,3,1]
    # Output: 0
    # Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
    # 1 <= prices.length <= 105
    # 0 <= prices[i] <= 104

# Topic: Sliding Window
# A sliding window is made using left and right pointers and expanded or shrinked according to need

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, result = 0, 0, 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            result = max(result, currentProfit)

            if prices[left] > prices[right]:
                left = right # shrinking the window from left
            right += 1

        return result