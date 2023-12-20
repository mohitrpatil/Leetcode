class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        remaining_money = money
        sorted_prices=sorted(prices)
        
        count = 0
        for i in range(len(sorted_prices)):
            if count<2 and (remaining_money - sorted_prices[i]) >=0:
                remaining_money = remaining_money - sorted_prices[i]
                # print(remaining_money)
                count += 1
                # print("C:", count)
            else:
                break
        
        if count==2:
            return remaining_money
        else:
            return money
        
        