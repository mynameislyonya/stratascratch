https://platform.stratascratch.com/coding/9892-second-highest-salary?code_type=1

select salary from (select *,
dense_rank() over(order by salary desc) rnk
from employee
) c
where rnk =2
