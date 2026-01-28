-- INNER JOIN en Microsoft Access
-- Muestra empleados con el nombre de su departamento

SELECT e.Nombre, d.Nombre AS Departamento, e.Salario
FROM Empleados e 
INNER JOIN Departamentos d ON e.Departamento_ID = d.ID;

