https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

with tab as (select *,lead(t) over(partition by user_id,timestamp::date) as next from(select *, 
first_value(timestamp) over(partition by user_id,timestamp::date,action order by timestamp desc) as t,
rank() over(partition by user_id,timestamp::date,action order by timestamp desc) as rnk

from facebook_web_log
where action in ('page_exit','page_load') and user_id in (select user_id
from facebook_web_log where action='page_exit')) x
where rnk=1 )

select user_id,avg(t-next) from tab 
where next is not null
group by user_id
