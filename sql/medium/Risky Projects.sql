https://platform.stratascratch.com/coding/10304-risky-projects?tabname=solutions

with tab as(select project_id ,sum((salary/365.0)) as s
from
linkedin_employees le 
join linkedin_emp_projects lep
on le.id=lep.emp_id
group by project_id
order by 1)

select title,budget,  CEILING((datediff('day',start_date,end_date)*s)) from linkedin_projects lp
join tab 
on lp.id=tab.project_id
where budget<round((datediff('day',start_date,end_date)*s)) 
