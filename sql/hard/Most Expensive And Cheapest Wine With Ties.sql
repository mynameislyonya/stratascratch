https://platform.stratascratch.com/coding/2147-most-expensive-and-cheapest-wine-with-ties?code_type=1

with tab as (select region_1 as reg, variety, price from winemag_pd
union all
select region_2 as reg, variety, price from winemag_pd),
exp as (select reg,variety from (select *,
dense_rank() over(partition by reg order by price desc) rnk
from tab 
where reg is not null and price is not null) x
where rnk=1),
low as (select reg,variety from (select *,
dense_rank() over(partition by reg order by price) rnk
from tab 
where reg is not null and price is not null) x
where rnk=1)

select distinct exp.reg,exp.variety as expensive,low.variety as cheapest from exp join low on exp.reg=low.reg

