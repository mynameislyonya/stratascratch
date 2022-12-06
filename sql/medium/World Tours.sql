https://platform.stratascratch.com/coding/2098-world-tours?code_type=1

with tab as(select *,
first_value(start_city) over(partition by traveler order by date asc) as t,
first_value(end_city) over(partition by traveler order by date desc) as e

from travel_history)

select count(distinct traveler) from tab
where t=e
