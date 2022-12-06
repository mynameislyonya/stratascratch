https://platform.stratascratch.com/coding/2036-lowest-revenue-generated-restaurants?code_type=1

select restaurant_id, total_amount
from
(select restaurant_id, sum(order_total) as total_amount, percent_rank() over (order by sum(order_total))rk
from doordash_delivery
where extract(month from customer_placed_order_datetime) = '05' and extract(year from customer_placed_order_datetime)= '2020'
group by restaurant_id
order by 3) a
where rk<=0.02
