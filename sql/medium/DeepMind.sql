https://platform.stratascratch.com/coding/10070-deepmind-employment-competition?code_type=1

select team_id,avg(member_score) from google_competition_scores s join google_competition_participants p
on s.member_id=p.member_id
group by team_id
order by 2 desc
