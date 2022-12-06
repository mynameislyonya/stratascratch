https://platform.stratascratch.com/coding/9624-accommodates-to-bed-ratio?code_type=1

select city,avg(accommodates::float/beds::float) from airbnb_search_details
where room_type = 'Shared room'
group by city 
order by 2 desc
