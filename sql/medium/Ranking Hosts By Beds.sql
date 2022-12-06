https://platform.stratascratch.com/coding/10161-ranking-hosts-by-beds?code_type=1

select
host_id,
sum(n_beds) AS sn,
dense_rank() over(ORDER BY sum(n_beds) DESC)


from airbnb_apartments
group by host_id
