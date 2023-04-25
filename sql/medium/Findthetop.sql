https://platform.stratascratch.com/coding/9979-find-the-top-5-highest-paid-and-top-5-least-paid-employees-in-2012?code_type=1

with h as (select * from (select employeename,totalpaybenefits, dense_rank() over(order by totalpaybenefits desc) rnk from sf_public_salaries
where year = 2012) x
where rnk<6),
l as (select * from (select employeename,totalpaybenefits, dense_rank() over(order by totalpaybenefits ) rnk from sf_public_salaries
where year = 2012) x
where rnk<6),

f as (select * from h
union
select * from l)

select employeename,totalpaybenefits from f
order by totalpaybenefits
