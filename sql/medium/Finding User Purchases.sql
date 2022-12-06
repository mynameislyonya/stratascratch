https://platform.stratascratch.com/coding/10322-finding-user-purchases?tabname=solutions

WITH TAB AS (select user_id,item,created_at, LAG(created_at) OVER(partition  BY user_id ORDER BY created_at DESC) AS next_buy
from amazon_transactions)

SELECT DISTINCT user_id
FROM TAB
WHERE next_buy-created_at<=7
