class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0
        for i in range(0,len(prices) - 1):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                if prices[r] - prices[l] > p:
                    p = prices[r] - prices[l]
                r += 1
        return p
                 
        