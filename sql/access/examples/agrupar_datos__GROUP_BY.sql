-- GROUP BY en Microsoft Access
-- Cuenta cuntos empleados hay en cada departamento

SELECT d.Nombre AS Departamento, COUNT(e.ID) AS Total_Empleados
FROM Empleados e
JOIN Departamentos d ON e.Departamento_ID = d.ID
GROUP BY d.Nombre;

-- Output:
-- Departamento      | Total_Empleados
-- -------------- | ----------------
-- Desarrollo        | 2
-- Ventas            | 2
-- Recursos Humanos  | 1