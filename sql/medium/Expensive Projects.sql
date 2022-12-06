https://platform.stratascratch.com/coding/10301-expensive-projects?code_type=1



with tab as (select project_id,count(*) as cnt from ms_emp_projects
group by project_id)


select budget/cnt from ms_projects l left join tab t on l.id=t.project_id
