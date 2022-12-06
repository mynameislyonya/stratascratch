https://platform.stratascratch.com/coding/9912-lowest-priced-orders?code_type=1

select c.id,first_name,min(total_order_cost) as t from customers c left join orders o
on c.id=o.cust_id

group by c.id,first_name
having min(total_order_cost)>0
