https://platform.stratascratch.com/coding/10068-user-email-labels?code_type=1

with tab as(select gge.to_user,ggl.label,count(day) as c from google_gmail_emails gge left join  google_gmail_labels ggl
on gge.id=ggl.email_id
where label in ('Promotion', 'Social','Shopping')
group by gge.to_user,ggl.label
order by to_user asc)

select to_user,
       sum(case when label = 'Promotion' then c else 0 end) as Promotion,
       sum(case when label = 'Social' then c  else 0  end) as Social,
       sum(case when label = 'Shopping'   then c else 0 end) as Shopping
from tab
group by to_user
order by to_user
