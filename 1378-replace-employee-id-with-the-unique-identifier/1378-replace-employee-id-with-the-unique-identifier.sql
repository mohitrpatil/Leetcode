# Write your MySQL query statement below


select e.unique_id, e1.name 
from Employees as e1
left join EmployeeUNI as e 
on e1.id = e.id