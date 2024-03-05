# Write your MySQL query statement below


SELECT s.product_id, p.product_name
FROM Sales AS s 
LEFT JOIN Product AS p ON s.product_id = p.product_id
group by s.product_id, p.product_name
having  max(s.sale_date) <= '2019-03-31' and min(s.sale_date) >= '2019-01-01'
