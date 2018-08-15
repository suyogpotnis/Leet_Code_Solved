"""
Source: LeetCode

121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:

# 1. Solution 1
    def maxProfit(self,prices):
        result = 0

        if len(prices) == 0:
            return 0

        minval = prices[0]
        for i in range(1,len(prices)):

            if minval > prices[i]:
                minval = prices[i]
            elif prices[i] - minval > result:
                result = prices[i] - minval
        return result

# 2. Solution 2 (inefficient as you have to use max for each iteration)

    def maxProfit(self, prices):

        result = 0

        if len(prices) == 0:
            return 0

        for i in range(0,len(prices)-1):

            if max(prices[i+1:len(prices)]) - prices[i] > result:
                result = max(prices[i+1:len(prices)]) - prices[i]
            else:
                pass
        return result
