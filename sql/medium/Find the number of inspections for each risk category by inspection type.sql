https://platform.stratascratch.com/coding/10130-find-the-number-of-inspections-for-each-risk-category-by-inspection-type?code_type=1


select inspection_type,
count(business_id) filter(where risk_category is null) as n_risk,
count(business_id) filter(where risk_category = 'Low Risk') as l_risk,
count(business_id) filter(where risk_category = 'Moderate Risk') as m_risk,
count(business_id) filter(where risk_category = 'High Risk') as h_risk,
count(business_id) as cnt
from sf_restaurant_health_violations
group by inspection_type
order by  cnt desc
