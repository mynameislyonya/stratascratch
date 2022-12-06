https://platform.stratascratch.com/coding/2047-total-monatery-value-per-monthservice?code_type=1


select date_part('month',order_date) as d,
sum(monetary_value) filter (where service_name = 'Uber_BOX') AS Uber_BOX,
sum(monetary_value) filter (where service_name = 'Uber_CLEAN') AS Uber_CLEAN,
sum(monetary_value) filter (where service_name = 'Uber_FOOD') AS Uber_FOOD,
sum(monetary_value) filter (where service_name = 'Uber_GLAM') AS Uber_GLAM,
sum(monetary_value) filter (where service_name = 'Uber_KILAT') AS Uber_KILAT,
sum(monetary_value) filter (where service_name = 'Uber_MART') AS Uber_MART,
sum(monetary_value) filter (where service_name = 'Uber_MASSAGE') AS Uber_MASSAGE,
sum(monetary_value) filter (where service_name = 'Uber_RIDE') AS Uber_RIDE,
sum(monetary_value) filter (where service_name = 'Uber_SEND') AS Uber_SEND,
sum(monetary_value) filter (where service_name = 'Uber_SHOP') AS Uber_SHOP,
sum(monetary_value) filter (where service_name = 'Uber_TIX') AS Uber_TIX

from uber_orders
where status_of_order = 'Completed'
group by date_part('month',order_date)
