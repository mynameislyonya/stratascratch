https://platform.stratascratch.com/coding/9632-host-popularity-rental-prices?code_type=1

with cte as(
            select distinct
                    case
                    when number_of_reviews <1 then 'New'
                    when 1<=number_of_reviews  and number_of_reviews<=5 then 'Rising'
                    when 6<=number_of_reviews  and number_of_reviews<=15  then 'Trending Up'
                    when 16<=number_of_reviews  and number_of_reviews<=40  then 'Popular'
                    when number_of_reviews > 40 then 'Hot'
                    end as popularity, 
                    price, room_type, host_since, zipcode, number_of_reviews
            from airbnb_host_searches
            )
select popularity, min(price), avg(price), max(price)
from cte
group by popularity
