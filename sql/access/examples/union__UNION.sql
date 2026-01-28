-- UNION en Microsoft Access
-- Combina nombres de empleados y nombres de departamentos (sin duplicados)

SELECT Nombre FROM Empleados
UNION
SELECT Nombre FROM Departamentos;

