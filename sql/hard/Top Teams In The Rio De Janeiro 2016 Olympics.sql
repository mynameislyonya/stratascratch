https://platform.stratascratch.com/coding/9960-top-teams-in-the-rio-de-janeiro-2016-olympics/solutions?code_type=1

with t as (select event,team,count(*) as n , row_number() over(partition by event order by team asc) as r from olympics_athletes_events
where year = 2016 and medal is not null
group by event,team), tab as
(select event,
    coalesce(max(case when  r= 1 then concat(team,  ' with ', n, ' medals') else null end),'No Team') as gold_team,
    coalesce(max(case when r = 2 then concat(team,  ' with ', n, ' medals') else null end),'No Team') as silver_team,
    coalesce(max(case when r = 3 then concat(team,  ' with ', n, ' medals') else null end),'No Team') as bronze_team
    from t 
group by event)

select * from tab
order by 1
