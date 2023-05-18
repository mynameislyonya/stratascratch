https://platform.stratascratch.com/coding/9952-name-to-medal-connection/solutions?code_type=1

select
    length(split_part(name,' ',1)),
    count(case when lower(medal) is null then 1 end) as no_medal,
    count(case when lower(medal)='bronze' then 1 end) as bronze,
    count(case when lower(medal)='silver' then 1 end) as silver,
    count(case when lower(medal)='gold' then 1 end) as gold
from 
    olympics_athletes_events
group by 1
