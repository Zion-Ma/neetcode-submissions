-- Write your query below
select name 
from customers c
where not exists (
    select customer_id
    from orders 
    where customer_id = c.id
)