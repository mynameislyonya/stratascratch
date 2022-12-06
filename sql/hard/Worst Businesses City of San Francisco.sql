https://platform.stratascratch.com/coding/9739-worst-businesses?code_type=1

select * from (select to_char(inspection_date,'yyyy'),business_name,
count(violation_id),
rank() over(partition by to_char(inspection_date,'yyyy') order by 
count(violation_id) desc 
) as rnk
from sf_restaurant_health_violations
group by to_char(inspection_date,'yyyy'),business_name) x
where rnk = 1
