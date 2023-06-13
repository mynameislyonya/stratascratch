https://platform.stratascratch.com/coding/2162-top-3-year-month-sales?code_type=1

select 
    sales_month, total_sales
from(
select to_char(order_date,'yyyy-mm') sales_month,
sum(order_value) total_sales,
dense_rank() over(order by sum(order_value) desc) rnk
from fct_customer_sales
    group by to_char(order_date,'yyyy-mm')
) x
where rnk<4
