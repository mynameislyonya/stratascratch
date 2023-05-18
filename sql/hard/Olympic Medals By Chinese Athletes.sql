https://platform.stratascratch.com/coding/9959-olympic-medals-by-chinese-athletes/solutions?code_type=1

select medal,
count(*) filter(where year=2000) as ol_2000,
count(*) filter(where year=2004) as ol_2004,
count(*) filter(where year=2008) as ol_2008,
count(*) filter(where year=2012) as ol_2012,
count(*) filter(where year=2016) as ol_2016,
count(*) as total
from olympics_athletes_events
where team = 'China'
group by medal
