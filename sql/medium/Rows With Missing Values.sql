https://platform.stratascratch.com/coding/2106-rows-with-missing-values?code_type=1

with tab as(select *,
row_number() over() as id
from user_flags), h as

(select id,
count(*) filter(where user_firstname is null) as a,
count(*) filter(where user_lastname is null) as b,
count(*) filter(where video_id is null) as c,
count(*) filter(where flag_id is null) as d
from tab
group by id), r as 
(select id,sum(a+b+c+d) as s from h
group by id
), q as

(select * from r
where s > 1)

select * from tab
where id in(select id from q)
