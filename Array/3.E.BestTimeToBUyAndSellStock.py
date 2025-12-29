class solution:
    def maxProfit(self,prices=[int]):
        

        min_price=float('inf')
        max_profit=0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price  - min_price

                if profit > max_profit :
                    max_profit = profit

        return max_profit


prices=[7,1,5,6,3,9]
sol = solution()
result = sol.maxProfit(prices)
print("max profit is:",result)