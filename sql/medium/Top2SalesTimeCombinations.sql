https://platform.stratascratch.com/coding/2154-top-2-busiest-sales-days?code_type=1

with tab as (select *,extract('hour' from timestamp) as hour, to_char(timestamp, 'Day') as day from sales_log),
tab1 as (select *,case when hour < 12 then 'Morning' 
when hour > 12 and hour <=15 then 'Early afternoon'
else 'Late afternoon' end as part
from tab )

select * from (select day,part,count(order_id),dense_rank() over(order by count(order_id) desc) as rnk from tab1
group by day,part) x
where rnk < 3
