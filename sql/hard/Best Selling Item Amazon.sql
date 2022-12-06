select
    date,
    description,
    total
from
    (select 
        date_part('month',invoicedate) as date,
        description,
        sum(unitprice*quantity) as total,
        row_number() over (partition by date_part('month', invoicedate)
        order by sum(unitprice * quantity) desc) as rnk
        from 
        online_retail
        group by date,description) x
where rnk = 1
