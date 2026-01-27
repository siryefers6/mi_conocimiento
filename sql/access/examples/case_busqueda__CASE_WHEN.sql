-- CASE búsqueda en Microsoft Access
SELECT nombre, CASE edad WHEN 25 THEN 'Joven' WHEN 30 THEN 'Adulto' ELSE 'Otro' END AS categoria FROM empleados;