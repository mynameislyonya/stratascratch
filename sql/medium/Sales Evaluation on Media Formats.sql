https://platform.stratascratch.com/coding/2158-sales-evaluation-on-media-formats/solutions?code_type=1

with t as (select 
product_family,
media_type,sum(units_sold*cost_in_dollars) as total from online_orders o
left join online_sales_promotions s
on o.promotion_id=s.promotion_id
left join online_products p
on o.product_id=p.product_id
group by product_family,media_type)

select 
    product_family,
    media_type,
    round(100 * total / sum(total) over(
        partition by product_family),0) as prct
from t
order by 1, 3
