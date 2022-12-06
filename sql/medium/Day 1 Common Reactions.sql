https://platform.stratascratch.com/coding/9773-day-1-common-reactions?code_type=1


select reaction,d from (select reaction,count(*) as d,
rank() over(order by count(*) desc) as rnk
from facebook_reactions
where date_day = 1
group by reaction) x
where rnk = 1
