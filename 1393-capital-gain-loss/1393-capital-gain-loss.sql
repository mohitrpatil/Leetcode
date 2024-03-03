# Write your MySQL query statement below

with buy as (
    select stock_name, sum(price) as buy
    from Stocks
    where operation = 'Buy'
    group by stock_name
),
 sell as(
    select stock_name, sum(price) as sell
    from Stocks
    where operation = 'Sell'
    group by stock_name
)

select b.stock_name, s.sell-b.buy as capital_gain_loss
from buy b
left join sell s
on b.stock_name = s.stock_name