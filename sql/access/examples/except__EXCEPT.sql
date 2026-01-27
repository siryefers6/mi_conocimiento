-- EXCEPT en Microsoft Access
-- Nota: Access no soporta EXCEPT; usar LEFT JOIN con IS NULL.
SELECT e.nombre FROM empleados e LEFT JOIN ex_empleados ex ON e.nombre = ex.nombre WHERE ex.nombre IS NULL;