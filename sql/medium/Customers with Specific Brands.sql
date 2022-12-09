https://platform.stratascratch.com/coding/2071-customers-with-specific-brands?code_type=1

select customer_id from facebook_products fp
left join facebook_sales fs
on fp.product_id=fs.product_id
where brand_name in ('Fort West','Golden')
group by customer_id
having count(distinct brand_name) = 2
