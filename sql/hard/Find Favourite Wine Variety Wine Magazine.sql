with t as(select taster_name,variety,count(*) as cnt from winemag_p2
where taster_name is not null
group by taster_name,variety
order by taster_name, cnt desc)

select taster_name,variety from
(select *,
dense_rank() over(partition by taster_name order by cnt desc) as rnk
from t) x
where rnk<2
