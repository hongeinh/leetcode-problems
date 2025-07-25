# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
with customer_orders as (
    select customer_number, count(*) as total_order
    from orders
    group by customer_number
)

select customer_number
from customer_orders
order by total_order desc
limit 1