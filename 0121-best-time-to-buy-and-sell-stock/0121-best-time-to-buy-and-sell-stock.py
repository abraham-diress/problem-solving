class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = float('inf')

        for price in prices:
            if price < cur_min:
                cur_min = price
            
            max_profit = max(max_profit, price - cur_min)

        return max_profit

        
        