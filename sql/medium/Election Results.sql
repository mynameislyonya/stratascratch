https://platform.stratascratch.com/coding/2099-election-results?code_type=1

select  candidate,sum(cnt)
from (select *,
count(*) over(partition by voter),
round(1/(count(*) over(partition by voter))::decimal ,3) as cnt
from voting_results
where candidate is not null) x
group by candidate
order by 2 desc
limit 1
