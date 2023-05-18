https://platform.stratascratch.com/coding/2135-actual-vs-predicted-arrival-time/solutions?code_type=1

select percentile_cont(0.9) within group(order by (actual_time_of_arrival - predicted_eta) / 60 asc) as ninetieth_percentile
from trip_details
where status = 'completed' and actual_time_of_arrival between '2022-01-01' and '2022-01-14'
;
