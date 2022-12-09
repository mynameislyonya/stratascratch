https://platform.stratascratch.com/coding/9740-daily-violation-counts?code_type=1

with tab as (select inspection_date,count(violation_id) as cnt,lag(count(violation_id)) over(order by inspection_date) as prev_cnt
from sf_restaurant_health_violations
group by inspection_date)

select inspection_date,cnt-prev_cnt from tab
