# Write your MySQL query statement below
with cte1 as (
select managerId, count(managerId) as c1
from Employee as e
group by managerId
having c1>=5
)

select e.name from cte1 as c
join Employee as e
on c.managerId = e.Id;
