class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = math.inf

        maxProfit = 0

        for idx, x in enumerate(prices):
            # when we find a val which is lower than the min, cal profit (or when last val)
            if x < minP:
                # calc profit
                profit = maxP - minP
                # update max profit
                maxProfit = max(maxProfit, profit)
                # reset min and max prices
                maxP = 0
                minP = x
            else:
                # update max
                maxP = max(maxP, x)
            
            print("minP: ", minP)
            print("maxP: ", maxP)
        
        # calc profit at end
        profit = maxP - minP
        # update max profit
        maxProfit = max(maxProfit, profit)
        
        return maxProfit
