https://platform.stratascratch.com/coding/2074-monthly-churn-rate?code_type=1

select
(count(user_id) filter(where contract_start <= '2021-09-01' and
(contract_end >= '2021-09-01' or contract_end IS NULL)) 
    - 
count(user_id) filter(where contract_start <= '2021-09-30' and
(contract_end >= '2021-09-30' or contract_end IS NULL)))
    /
count(user_id) filter(where contract_start <= '2021-09-01' and
(contract_end >= '2021-09-01' or contract_end IS NULL))::float 
* 100                          

from
    natera_subscriptions
