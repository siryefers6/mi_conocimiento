-- CASE simple en Microsoft Access
SELECT nombre, CASE WHEN edad > 30 THEN 'Mayor' ELSE 'Menor' END AS categoria FROM empleados;