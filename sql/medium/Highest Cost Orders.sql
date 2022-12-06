https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1

select first_name,sum(total_order_cost) as num,order_date from customers c  left join orders o on c.id=o.cust_id
where order_date between '2019-02-01' and '2019-05-01'
group by first_name,order_date
order by num desc
limit 1
