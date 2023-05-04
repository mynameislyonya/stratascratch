https://platform.stratascratch.com/coding/2157-10-monthly-sales-increase/solutions?code_type=1

with m as (select product_id,sum(cost_in_dollars*units_sold) as sold_may from online_orders
where extract('month' from date) = 5
group by product_id ),
a as (select product_id,sum(cost_in_dollars*units_sold) as sold_april from online_orders
where extract('month' from date) = 4
group by product_id )

select m.product_id,(sold_may-sold_april)/sold_april*100 from a join m on a.product_id = m.product_id
where 100*(sold_may-sold_april)/sold_april>10
