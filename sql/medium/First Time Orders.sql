https://platform.stratascratch.com/coding/2093-first-time-orders?code_type=1

with tab as(select name,count(*) as f from (select *,
first_value(order_timestamp) over(partition by customer_id order by order_timestamp) as d
from doordash_orders 
left join doordash_merchants dm
on doordash_orders.merchant_id=dm.id
order by 2) x
where order_timestamp=d
group by name),

tab1 as (select name,count(*) as a
from doordash_orders 
left join doordash_merchants dm
on doordash_orders.merchant_id=dm.id
group by name
order by 2)

select tab1.name,a,

coalesce(f,0) from tab1 left join tab on tab1.name=tab.name
