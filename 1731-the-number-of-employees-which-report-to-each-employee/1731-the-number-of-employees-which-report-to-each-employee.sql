# Write your MySQL query statement below
select e2.employee_id, e2.name , count(e.employee_id) as reports_count,
round(avg(e.age)) as average_age
from employees e
left join employees e2
on e.reports_to = e2.employee_id
where e2.employee_id is not null
group by e2.employee_id, e2.name
order by e2.employee_id;