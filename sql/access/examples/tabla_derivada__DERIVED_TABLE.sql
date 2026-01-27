-- Tabla derivada en Microsoft Access
SELECT * FROM (SELECT nombre, edad FROM empleados) AS sub;