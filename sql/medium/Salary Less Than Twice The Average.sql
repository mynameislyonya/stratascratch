https://platform.stratascratch.com/coding/2110-salary-less-than-twice-the-average?code_type=1

with t as(select manager_empl_id,avg(salary) as av from dim_employee de left join map_employee_hierarchy meh
on de.empl_id=meh.empl_id
group by manager_empl_id)

select manager_empl_id,salary,av from t left join 
dim_employee de
on t.manager_empl_id=de.empl_id
where salary< av*2
