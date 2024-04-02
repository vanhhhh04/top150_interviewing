# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# class Solution:
#     def maxProfit(self, prices) -> int:
#         profit = 0
#         buy = prices[0]
#         for i in range(1, len(prices)):
#             if buy < prices[i]:
#                 profit += prices[i] - buy
#             buy = prices[i]
#         return profit












class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > buy :
                profit += prices[i] - buy
            buy = prices[i]
        return profit




prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))






