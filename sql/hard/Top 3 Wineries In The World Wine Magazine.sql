https://platform.stratascratch.com/coding/10042-top-3-wineries-in-the-world?tabname=question


with t as(select * from (select country,
winery,
avg(points) as p,
row_number() over(partition by country order by avg(points) desc,winery) as rnk
from 
winemag_p1
group by 
country, winery) x 
where rnk<4), 
h as (select *,
winery || ' (' || round(p) || ')' as best
,
lead(winery || ' (' || round(p) || ')' ) over(partition by country) as second,
lead(winery || ' (' || round(p) || ')',2) over(partition by country) as third
from t)

select country,
       best as top_winery,
       coalesce(second, 'No second winery') AS second_winery,
       coalesce(third, 'No third winery') AS third_winery FROM h
where rnk=1
order by country
