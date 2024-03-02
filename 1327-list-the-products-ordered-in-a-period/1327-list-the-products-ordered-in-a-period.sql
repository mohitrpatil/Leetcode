# Write your MySQL query statement below

with valid_orders as (
    select * 
    from orders 
    where extract(year from order_date) = '2020' 
    and extract(month from order_date) = '02'
),

cte as (
    select p.product_id, p.product_name, o.order_date, o.unit 
    from products as p
    left join valid_orders as o
    on p.product_id = o.product_id
)

select product_name, sum(unit) as unit 
from cte
group by product_name
having unit >= 100;