https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=1

select 'bear',count(*) from google_file_store
where contents like '%bear%'
UNION
select 'bull',count(*) from google_file_store
where contents like '%bull%'
