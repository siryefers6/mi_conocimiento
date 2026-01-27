-- INTERSECT en Microsoft Access
-- Nota: Access no soporta INTERSECT; usar INNER JOIN o EXISTS.
SELECT DISTINCT e.nombre FROM empleados e INNER JOIN ex_empleados ex ON e.nombre = ex.nombre;