SELECT 
    ca.ca_state AS state,
    COUNT(c.c_customer_sk) AS customer_count
FROM 
    customer c
JOIN 
    customer_address ca ON c.c_current_addr_sk = ca.ca_address_sk
WHERE 
    ca.ca_state IS NOT NULL
GROUP BY 
    ca.ca_state
ORDER BY 
    customer_count DESC
LIMIT 5;