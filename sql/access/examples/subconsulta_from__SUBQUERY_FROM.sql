-- Subconsulta en FROM en Microsoft Access
SELECT avg_edad FROM (SELECT AVG(edad) AS avg_edad FROM empleados) AS sub;