# Write your MySQL query statement below

with cte as (
select * from 
(select *,
rank() over( partition by product_id order by year asc) as r1
from
sales) as X
where X.r1 = 1)

select product_id, year as first_year, quantity, price
from cte
;