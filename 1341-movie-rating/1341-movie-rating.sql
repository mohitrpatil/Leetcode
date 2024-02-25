# Write your MySQL query statement below

with cte1 as (
select u.name from (select user_id, count(movie_id) as cnt
from movierating
group by user_id) as X
left join Users as u
on x.user_id = u.user_id
order by x.cnt desc, u.name
limit 1),

cte2 as 
(select m.title from
(select movie_id , avg(rating) as avg1
from movierating
where month(created_at) = '02' and year(created_at) = '2020'
group by movie_id) as x
left join Movies as m
on x.movie_id = m.movie_id
order by x.avg1 desc, m.title asc
limit 1)

select name as results from cte1
union all
select title as results from cte2;