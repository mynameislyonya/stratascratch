https://platform.stratascratch.com/coding/2155-ad-performance-rating?code_type=1

with tab as (select product_id,sum(quantity) as total from marketing_campaign
group by product_id
order by 2 desc)

select *, case when total > 30 then 'Outstanding'
when total between 20 and 29  then 'Satisfactory'
when total between 10 and 19 then 'Unsatisfactory'
when total between 1 and 9 then 'Poor'
end
from tab
