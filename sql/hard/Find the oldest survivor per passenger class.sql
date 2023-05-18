https://platform.stratascratch.com/coding/9883-find-the-oldest-survivor-per-passenger-class?code_type=1

select pclass, name, age from (select *, dense_rank() over(partition by pclass order by age desc) as rnk from titanic
where survived = 1 and age is not null) x 
where rnk = 1
