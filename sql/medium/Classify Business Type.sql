https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=1

select distinct business_name,
case
when lower(business_name) ilike '%restaurant%' then 'restaurant'
when lower(business_name) ~ 'cafe|café|coffee' then 'cafe'
when lower(business_name) ilike '%School%' then 'school'
else 'other'
end
from sf_restaurant_health_violations

