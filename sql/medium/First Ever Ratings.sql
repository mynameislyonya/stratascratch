https://platform.stratascratch.com/coding/2114-first-ever-ratings?code_type=1

select ((select count(*) from(select *,
first_value(actual_delivery_time) over(partition by dasher_id order by actual_delivery_time) as d
from delivery_orders) x 
where actual_delivery_time=d and delivery_rating = 0)::float/
(select count(*) from(select *,
first_value(actual_delivery_time) over(partition by dasher_id order by actual_delivery_time) as d
from delivery_orders) x 
where actual_delivery_time=d)::float)*100
