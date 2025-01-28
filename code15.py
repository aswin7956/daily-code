#best time to buy and sell stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=float("inf") #to store min price a stock can get
        ma=0 #to store max profit ater stock is brought
        for i in prices:
            if i<mi: #if a new low price is encountered then change it to be min
                mi=i
            ma=max(ma,i-mi) #update max profit iteratively through the array
        return ma 