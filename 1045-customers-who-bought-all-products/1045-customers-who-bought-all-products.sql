# Write your MySQL query statement below

with cte as (select c.customer_id, c.product_key
from Customer c
cross join Product p)

select x.customer_id
from (
select c1.customer_id, 
count(distinct c.product_key) / (select count(product_key) from Product) as p
from cte as c1
join customer as c
on c1.customer_id = c.customer_id and c1.product_key = c.product_key
group by c1.customer_id) as x
where x.p =1
;