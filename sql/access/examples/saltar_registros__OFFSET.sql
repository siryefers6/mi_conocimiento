-- OFFSET en Microsoft Access
-- Nota: Access no soporta OFFSET directamente; usar subconsulta o TOP con orden.
-- Ejemplo aproximado con subconsulta.
SELECT * FROM empleados WHERE id NOT IN (SELECT TOP 5 id FROM empleados ORDER BY id);