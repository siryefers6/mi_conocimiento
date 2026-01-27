-- Subconsulta en WHERE en Microsoft Access
SELECT * FROM empleados WHERE edad > (SELECT AVG(edad) FROM empleados);