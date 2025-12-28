-- Identificar las top 5 categorías por volumen de inventario (valor potencial)--
SELECT 
    category,
    COUNT(product_id) as total_products,
    ROUND(AVG(actual_price), 2) as avg_price,
    SUM(actual_price) as total_inventory_value
FROM amazon_products
GROUP BY category
ORDER BY total_inventory_value DESC
LIMIT 5;



-- Analizar si un descuento alto impacta la satisfacción del cliente
SELECT 
    CASE 
        WHEN discount_percentage > 50 THEN 'High Discount (>50%)'
        WHEN discount_percentage BETWEEN 20 AND 50 THEN 'Medium Discount (20-50%)'
        ELSE 'Low Discount (<20%)'
    END as discount_segment,
    ROUND(AVG(rating), 2) as avg_rating,
    COUNT(*) as total_sales
FROM amazon_products
GROUP BY 1
ORDER BY avg_rating DESC;