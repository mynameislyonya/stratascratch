https://platform.stratascratch.com/coding/10351-activity-rank?code_type=1

select from_user,
count(*) as c,
row_number() over(order by count(*) desc,from_user)
from google_gmail_emails
group by from_user
