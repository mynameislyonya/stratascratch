https://platform.stratascratch.com/coding/9910-favorite-customer?code_type=1

select first_name,
city,
sum(total_order_cost) as total,
count(total_order_cost) as cnt
from customers c left join orders o on c.id=o.cust_id
group by first_name,city
having sum(total_order_cost)>100 and count(total_order_cost)>3
