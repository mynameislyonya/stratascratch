https://platform.stratascratch.com/coding/9700-rules-to-determine-grades?code_type=1

select grade,min(score),max(score),
'Score > ' || min(score)-1 || ' AND Score <= ' || max(score)|| ' => Grade = ' || grade as "rule"

from los_angeles_restaurant_health_inspections
group by grade
order by grade
