# Write your MySQL query statement below
with cte as(
    select e.name as Employee, e.salary, d.name as Department
    from Employee as e
    left join Department as d
    on e.departmentId = d.id
)

select Department, Employee, Salary 
from (select Employee, Salary, Department,
dense_rank() over (partition by Department order by salary desc) as dr
from cte) as X
where X.dr <= 3;