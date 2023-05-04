https://platform.stratascratch.com/coding/2041-total-sales-in-different-currencies?code_type=1

with rate as (select * from sf_exchange_rate
where date between '2020-01-01' and '2020-06-01'),
sales as(
select * from sf_sales_amount
where sales_date between '2020-01-01' and '2020-06-01')

select extract(quarter from sales_date) as quarter,sum(exchange_rate*sales_amount) from sales s join rate r on r.source_currency = s.currency and
r.date = s.sales_date
group by extract(quarter from sales_date)
