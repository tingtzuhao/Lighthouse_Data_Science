SELECT
product_name,
group_name,
price,
LEAD(price, 1) OVER (
    PARTITION BY group_name
    ORDER BY price 
) AS next_price,
price - LEAD(price, 1) OVER(
    PARTITION BY group_name
    ORDER BY price
) AS cur_next_diff

FROM products
JOIN product_groups USING(group_id)