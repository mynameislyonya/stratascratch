https://platform.stratascratch.com/coding/2020-call-declines?code_type=1

with tab as(select company_id,
count(distinct ru.user_id) filter(where to_char(date,'YYYY-MM') = '2020-03') as mart,
count(distinct ru.user_id) filter(where to_char(date,'YYYY-MM') = '2020-04') as april
from rc_calls rc left join rc_users ru
on 
rc.user_id = ru.user_id

group by company_id)

select company_id,april-mart from tab 
order by 2 
limit 1
