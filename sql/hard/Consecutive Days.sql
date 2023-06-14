https://platform.stratascratch.com/coding/2054-consecutive-days?code_type=1

with a as (
    select *,
        lag(date, 1) over (partition by user_id order by date) as lag1,
        lag(date, 2) over (partition by user_id order by date) as lag2
    from sf_events
)
select user_id
from a 
where date = lag1 + interval '1 day' and lag1 = lag2 + interval '1 day';
