class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price, maximum_price = prices[0], 0
        for i in range(1, len(prices)):
            minimum_price = min(prices[i], minimum_price)
            maximum_price = max(prices[i] - minimum_price, maximum_price)
        return maximum_price
        