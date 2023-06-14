https://platform.stratascratch.com/coding/10084-cum-sum-energy-consumption?code_type=1

with tab as (select * from fb_eu_energy
union all
select * from fb_na_energy
union all
select * from fb_asia_energy),
tab1 as (select date,
sum(consumption) as consumption,
sum(sum(consumption)) over() as total
from tab
group by date
order by 1)

select date,sum(consumption) over(order by date),round(sum(consumption) over(order by date)/total*100) from tab1
