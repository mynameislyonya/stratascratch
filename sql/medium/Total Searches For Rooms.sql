https://platform.stratascratch.com/coding/9638-total-searches-for-rooms?code_type=1

select 
city,
count(*) FILTER(WHERE room_type = 'Entire home/apt'),
count(*) FILTER(WHERE room_type = 'Private room'),
count(*) FILTER(WHERE room_type = 'Shared room')
from airbnb_search_details
group by city
