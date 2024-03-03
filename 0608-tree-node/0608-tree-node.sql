# Write your MySQL query statement below

select
id,
case when p_id is NULL then 'Root'
when p_id in (select distinct id from Tree) and id in (select p_id from tree) then 'Inner'
else 'Leaf' end as type
from Tree;