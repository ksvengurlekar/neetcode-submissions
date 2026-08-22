class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buy
        r = 1 #sell
        maxprof = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxprof = max(maxprof, prices[r] - prices[l])
            
            r += 1

        return maxprof