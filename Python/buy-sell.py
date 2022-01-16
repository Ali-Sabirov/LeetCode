class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        print(n)
        profit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1]-prices[i])
                print('i', i, ':profit ', profit)
        print(profit)
        return profit