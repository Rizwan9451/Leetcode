class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        mx=0
        for i in range(1,len(prices)):
            if(buy>prices[i]):
                buy=prices[i]
            elif(prices[i]-buy>mx):
                mx=prices[i]-buy
        return mx


            

