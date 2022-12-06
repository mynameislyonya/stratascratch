https://platform.stratascratch.com/coding/2032-signups-by-billing-cycle?code_type=1


select extract(dow from signup_start_date) as weekday,


count(distinct case when billing_cycle = 'monthly' then signup_id end) as m,
count(distinct case when billing_cycle = 'annual' then signup_id end) as a,
count(distinct case when billing_cycle = 'quarterly' then signup_id end) as quarterly
from signups as s
join plans as p
on p.id = s.plan_id
group by weekday;
