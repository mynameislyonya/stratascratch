https://platform.stratascratch.com/coding/2096-completed-tasks?tabname=question

select aa.user_id,coalesce(sum(case when action_name = 'CompleteTask' 
        then num_actions else null end),0) from asana_users au
left join asana_actions aa
on au.user_id=aa.user_id
where to_char(date,'yyyy-mm') = '2022-01' and company = 'ClassPass'
group by aa.user_id
