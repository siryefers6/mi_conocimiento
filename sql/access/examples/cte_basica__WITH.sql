-- CTE en Microsoft Access
-- Nota: Access no soporta WITH (CTE); usar subconsulta.
SELECT * FROM (SELECT nombre FROM empleados) AS cte;