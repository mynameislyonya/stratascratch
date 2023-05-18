https://platform.stratascratch.com/coding/9955-norwegian-alpine-skiers?code_type=1

select distinct name from olympics_athletes_events
where team = 'Norway' 
and sport = 'Alpine Skiing' 
and year = 1992 
and name not in (select name from olympics_athletes_events where year = 1994)
