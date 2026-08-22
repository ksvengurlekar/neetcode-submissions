class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, n = 0, len(prices)
        maxp = 0
        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            
            maxp = max(maxp, prices[r] - prices[l])

        return maxp