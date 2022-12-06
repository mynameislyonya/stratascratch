https://platform.stratascratch.com/coding/2042-employees-years-in-service?code_type=1

with tab as(select 
*,
coalesce(termination_date,'2021-05-01') as dd,
case when termination_date is null then 'YES' else 'NO' end as still_employed
from uber_employees
where  (COALESCE(termination_date, '2021-05-01') - hire_date) > 730
)

select first_name,last_name,
(datediff('day',hire_date,dd)::float)/365 as years_spent,
still_employed
from tab
