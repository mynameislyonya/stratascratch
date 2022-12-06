https://platform.stratascratch.com/coding/10019-find-the-probability-of-ordering-a-ride-based-on-the-weather-and-the-hour?tabname=discussion

with t as (select
weather,
hour,
count(weather) as cn,
sum(count(weather)) over() as cnt
from lyft_rides
group by weather,hour)

select weather,hour,cn/cnt from t 
order by 1,2
