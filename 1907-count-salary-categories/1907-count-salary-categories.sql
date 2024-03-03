# Write your MySQL query statement below

select "Low Salary" as Category, count(*) as accounts_count
from Accounts 
where income < 20000
union all
select "Average Salary" as Category, count(*) as accounts_count
from Accounts 
where income >= 20000 and income <= 50000
union all 
select "High Salary" as Category, count(*) as accounts_count
from Accounts 
where income > 50000
