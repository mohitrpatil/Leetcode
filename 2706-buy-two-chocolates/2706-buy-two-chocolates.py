class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        remaining_money = money
        sorted_prices=sorted(prices)
        
        count = 0
        remaining_money = money - sorted_prices[0] - sorted_prices[1]
        
        if remaining_money >= 0:
            return remaining_money
        else:
            return money
        
        