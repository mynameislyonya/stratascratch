https://platform.stratascratch.com/coding/2104-user-with-most-approved-flags?code_type=1

with tab as (select 
concat(user_firstname,' ',user_lastname) as full_name,
count(distinct video_id) filter(where reviewed_outcome='APPROVED') as cnt

from user_flags uf inner join flag_review fr
on uf.flag_id=fr.flag_id
group by concat(user_firstname,' ',user_lastname))

select * from (select *,
rank() over( order by cnt desc) as rnk from tab) x 
where rnk = 1
