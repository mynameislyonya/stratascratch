https://platform.stratascratch.com/coding/9957-find-how-the-average-male-height-changed-between-each-olympics-from-1896-to-2016/solutions?code_type=1

select year, avg(height) as avg_height, 
coalesce(lag(avg(height),1) over (order by year),172.73) as 
prev_avg_height, avg(height) - coalesce(lag(avg(height),1) over (order by year),172.73) as diff
from (select distinct id, sex, age, height, weight, year from olympics_athletes_events) tab
where sex='M'
group by year
order by year;
