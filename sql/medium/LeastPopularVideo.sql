https://platform.stratascratch.com/coding/2161-least-popular-video?code_type=1

select video_id from (select video_id,count(distinct user_id),dense_rank() over(order by count(distinct user_id)) as rnk  from videos_watched
group by video_id) x
where rnk = 1
