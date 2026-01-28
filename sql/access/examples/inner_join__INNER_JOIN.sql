-- INNER JOIN en Microsoft Access
-- Muestra empleados con el nombre de su departamento

SELECT e.Nombre, d.Nombre AS Departamento, e.Salario
FROM Empleados e 
INNER JOIN Departamentos d ON e.Departamento_ID = d.ID;

-- Output:
-- Nombre          | Departamento      | Salario
-- --------------- | ----------------- | -------
-- Juan García     | Desarrollo        | 3500
-- Carlos Rodríguez| Desarrollo       | 3800
-- María López     | Ventas            | 4200
-- Pedro Sánchez   | Ventas            | 3900
-- Ana Martínez    | Recursos Humanos  | 4500