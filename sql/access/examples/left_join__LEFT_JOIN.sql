-- LEFT JOIN en Microsoft Access
-- Muestra todos los empleados y sus departamentos (si los tienen)

SELECT e.Nombre, d.Nombre AS Departamento
FROM Empleados e 
LEFT JOIN Departamentos d ON e.Departamento_ID = d.ID;

-- Output:
-- Nombre           | Departamento
-- -------------- | -----------------
-- Juan García     | Desarrollo
-- María López     | Ventas
-- Carlos Rodríguez | Desarrollo
-- Ana Martínez    | Recursos Humanos
-- Pedro Sánchez   | Ventas