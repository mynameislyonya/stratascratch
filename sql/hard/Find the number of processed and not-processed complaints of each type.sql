https://platform.stratascratch.com/coding/9790-find-the-number-of-processed-and-not-processed-complaints-of-each-type?code_type=1

select type, count(*) filter(where processed=True)  as processed, count(*) filter(where processed=False)as non_processed from facebook_complaints
group by type
