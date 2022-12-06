https://platform.stratascratch.com/coding/9919-unique-highest-salary?code_type=1

select * from (select salary,count(*) as cnt from employee
group by salary
order by 1 desc) x
where cnt = 1
limit 1
