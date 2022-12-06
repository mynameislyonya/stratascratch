https://platform.stratascratch.com/coding/2060-manager-of-the-largest-department?code_type=1

with t as(select department_id,
count(*),
rank() over(order by count(*) desc) as rnk
from az_employees
group by department_id)

select first_name,last_name from az_employees
where position ilike '%manager%' and department_id in (select department_id from t
where rnk = 1)
