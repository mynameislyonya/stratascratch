https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=1

select 
  state,num
from 
  (select state,
  count(city) as num,
  dense_rank() over(order by count(city) desc) rnk 
  from yelp_business
  where stars= 5
  group by state
  order by num desc) x
where x.rnk<5
