class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        print(n)
        p = 0
        s = False
        price = 0
        for i in range(n-1):
            if prices[i] < prices[i+1] and s==False:
                p -= prices[i]
                price = prices[i]
                print('i', i, ':buy ', prices[i], ' p =', p)
                s = True
            if prices[i] > prices[i+1] and s==True:
                p += prices[i]
                print('i', i, ':sell ', prices[i], ' p =', p)
                s = False
        print(p)
        return p