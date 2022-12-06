https://platform.stratascratch.com/coding/10124-bookings-vs-non-bookings?code_type=1

select case when ac.ts_booking_at is null then 'does not book'
else 'books' end,avg(n_searches)
from airbnb_searches ais
left join  airbnb_contacts ac
on ac.id_guest=ais.id_user and
ac.ds_checkin=ais.ds_checkin
group by 1
