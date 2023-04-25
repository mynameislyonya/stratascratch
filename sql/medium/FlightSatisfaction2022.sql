https://platform.stratascratch.com/coding/2144-flight-satisfaction-2022?code_type=1

select
s.class,
round(sum(s.satisfaction)/count(s.cust_id)) as avg_pct
from
survey_results s
join loyalty_customers c
on s.cust_id = c.cust_id
where c.age between 30 and 40
group by s.class
