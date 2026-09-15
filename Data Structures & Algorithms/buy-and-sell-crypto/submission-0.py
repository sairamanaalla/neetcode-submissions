class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxi=101
        for i in range(len(prices)):
            if prices[i] < maxi:
                maxi = prices[i]
            else:
                profit = max(profit, prices[i]- maxi)
        return profit
        