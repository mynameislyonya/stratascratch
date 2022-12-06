https://platform.stratascratch.com/coding/2048-percentage-of-revenue-loss?code_type=1

with tab as(select service_name,
sum(monetary_value) filter(where status_of_order <> 'Completed') as nc,
sum(monetary_value) as t,
sum(number_of_orders) filter(where status_of_order <> 'Completed') as c,
sum(number_of_orders) as nt

from uber_orders

group by service_name )

select service_name,
(c/nt)*100 as ntc,
(nc/t)*100 AS nct from tab
