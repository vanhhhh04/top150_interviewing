# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
        # for i in range(0,len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[i] > prices[j]:
        #             continue
        #         else :
        #             flag = False
        #             break
        #     if flag == False :
        #         break
        #     else :
        #         continue

        # if flag == True :
        #     return 0
        # else :
        # maximum = 0
        # for i in range(0,len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if (prices[j] - prices[i]) > maximum:
        #             maximum = prices[j] - prices[i]
        # if maximum == 0 :
        #     return 0
        # else :
        #     return maximum

    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell``
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


prices = [7,1,5,3,6,4]
s = Solution()
s.maxProfit(prices)








