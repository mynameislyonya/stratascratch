https://platform.stratascratch.com/coding/2016-pizza-partners?code_type=1

select pp.name,avg(amount)
from
postmates_orders po 
left join 
postmates_markets pm 
on po.city_id=pm.id
left join 
postmates_partners pp
on po.seller_id=pp.id
where pp.name ilike '%Pizza%' and pm.name='Boston'
group by pp.name
