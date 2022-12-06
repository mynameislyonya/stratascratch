https://platform.stratascratch.com/coding/9701-3rd-most-reported-health-issues?code_type=1


with third_category as(
select  pe_description,rnk from (
select 

pe_description,
count(*), dense_rank()over(order by count(*) desc) as rnk

from los_angeles_restaurant_health_inspections
where lower(facility_name) ilike '%cafe%' or 
lower(facility_name) ilike '%tea%' or 
lower(facility_name) ilike '%juice%'

group by pe_description)k where rnk = 3)


select u.facility_name from los_angeles_restaurant_health_inspections u join
third_category t on u.pe_description = t.pe_description

where lower(facility_name) ilike '%cafe%' or 
lower(facility_name) ilike '%tea%' or 
lower(facility_name) ilike '%juice%'
