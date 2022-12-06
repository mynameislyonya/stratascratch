https://platform.stratascratch.com/coding/10043-median-price-of-wines?tabname=solutions

with tab as (
select variety, price
from winemag_p1
union all
select variety, price
from winemag_p2
)

select variety,percentile_cont(0.5) within group(order by price) from tab
group by variety
