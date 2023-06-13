https://platform.stratascratch.com/coding/2164-stock-codes-with-prices-above-average?code_type=1

with t as (
select productcode, unitprice, 
    dense_rank() over (partition by productcode order by invoicedate) as rnk
from online_retails
where quantity > 0
)

select distinct productcode, unitprice
from t 
where rnk=1 and unitprice > (select avg(unitprice) from t)
order by 1,2
