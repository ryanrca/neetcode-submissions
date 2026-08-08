class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        max_price = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_price = max(max_price, profit)
            else:
                l = r
            r += 1

        return max_price
