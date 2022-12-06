https://platform.stratascratch.com/coding/10073-favorite-host-nationality?code_type=1

with tab as(select * from (select *,
dense_rank() over(partition by from_user order by review_score desc)
as rnk
from airbnb_reviews ar
where from_type='guest') x
where rnk = 1)

select distinct from_user,nationality from tab t
inner join airbnb_hosts ah
on t.to_user=ah.host_id
order by 1
