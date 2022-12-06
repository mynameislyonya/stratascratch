https://platform.stratascratch.com/coding/9716-top-3-facilities?code_type=1

with t as
(select owner_name,facility_address,
row_number() over(partition by owner_name order by avg(score) desc) as rnk
from los_angeles_restaurant_health_inspections
group by owner_name, facility_address
order by owner_name, avg(score) DESC) 


select owner_name,
max(case when rnk=1 then facility_address  end) AS best_score,
max(case when rnk=2 then facility_address  end)  AS second_score,
max(case when rnk=3 then facility_address  end) AS third_score
from t
group by owner_name
order by owner_name
