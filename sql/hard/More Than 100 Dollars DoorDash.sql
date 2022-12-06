/*
More Than 100 Dollars
[HeySushil - YouTube](https://platform.stratascratch.com/coding/2115-more-than-100-dollars?code_type=1)
Difficulty: Hard
For each month of 2021, calculate what percentage of restaurants, out of these that fulfilled any orders in a given month, fulfilled more than 100$ in monthly sales?
*/

with tab as(
  select 
    distinct date_part('month',order_placed_time) as dt,
    sum(count(distinct restaurant_id)) over(partition by date_part('month',order_placed_time)) as s
  from
    delivery_orders
  left join
    order_value ov
  on
    delivery_orders.delivery_id=ov.delivery_id
  where to_char(order_placed_time, 'yyyy') = '2021'
  group by date_part('month',order_placed_time),restaurant_id
  having sum(sales_amount)>100),
t as (
  select 
    date_part('month',order_placed_time) as dt,
    count(distinct restaurant_id) as c
  from
    delivery_orders
  left join
    order_value ov
  on
    delivery_orders.delivery_id=ov.delivery_id
  where to_char(order_placed_time, 'yyyy') = '2021'
  group by date_part('month',order_placed_time)
)

select t.dt,s/c*100
from tab left join t on tab.dt=t.dt

