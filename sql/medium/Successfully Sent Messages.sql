https://platform.stratascratch.com/coding/9777-successfully-sent-messages?code_type=1


select (select count(*) filter(where receiver is not null) from facebook_messages_sent fms
left join facebook_messages_received fmr
on fms.message_id=fmr.message_id)
/
(select count(*) from facebook_messages_sent fms
left join facebook_messages_received fmr
on fms.message_id=fmr.message_id)::float
