class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(0,len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] < prices[j]:
        #             profit = prices[j] - prices[i]
        #             max_profit = max(max_profit,profit)
        #             print(f"I {i}, J {j}")
        #             print(f"Prices_i {prices[i]}, Prices_j {prices[j]}")
        #             print(f"Profit {profit}")
        #             print(f"Max profit {max_profit}")

        # return max_profit
        max_profit  = 0
        min_price = 1000
        for i in range(0,len(prices)):
            min_price = min(min_price,prices[i])
            print(f"{i} price {prices[i]} --min {min_price}")
            max_profit = max(max_profit,prices[i]-min_price)
            print(f"max {max_profit}")
        return max_profit
        