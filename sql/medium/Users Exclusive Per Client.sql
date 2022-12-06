https://platform.stratascratch.com/coding/2025-users-exclusive-per-client?code_type=1

select client_id, count(distinct user_id) from fact_events
where user_id in (
select user_id from fact_events
group by 1
having count(distinct client_id)=1)
group by 1
order by 2 desc
