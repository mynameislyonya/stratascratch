https://platform.stratascratch.com/coding/2015-city-with-the-highest-and-lowest-income-variance?code_type=1

with t as (select name,order_timestamp_utc::date,sum(amount) as num
from postmates_orders po
left join 
postmates_markets pm
on po.city_id=pm.id
where to_char(order_timestamp_utc,'YYYY-MM-DD')  = '2019-03-11' or 
to_char(order_timestamp_utc,'YYYY-MM-DD')  = '2019-04-11'
group by name,order_timestamp_utc::date),
g as(select *,
lead(num) over(PARTITION  by name) as next
from t),

gg as (select name,(next-num) as t from g
where next is not null)

select name,t from gg
where t = (select max(t) from gg) or t = (select min(t) from gg)
