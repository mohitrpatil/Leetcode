# Write your MySQL query statement below

select max(x.num) as num from
(select num, count(num) as c1
from MyNumbers
group by num) as x
where x.c1=1;