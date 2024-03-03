# Write your MySQL query statement below

with cte as (
    select * from (
    select *,
    count(*) over (partition by lon, lat) as r1,
    count(*) over (partition by tiv_2015) as ct 
    from Insurance) as Y
)


select 
Round(sum(tiv_2016),2) as tiv_2016
from cte
where ct>1
and r1 =1;