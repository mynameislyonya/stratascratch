https://platform.stratascratch.com/coding/9817-find-the-number-of-times-each-word-appears-in-drafts/solutions?code_type=1

select words, count(*)
from(
select lower(trim(unnest(string_to_array(contents, ' ')), '.,')) as words
from google_file_store
where filename like '%draft%') t1
group by words
