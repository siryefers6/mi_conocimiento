-- UNION en Microsoft Access
-- Combina nombres de empleados y nombres de departamentos (sin duplicados)

SELECT Nombre FROM Empleados
UNION
SELECT Nombre FROM Departamentos;

-- Output:
-- Nombre
-- ----
-- Ana Martínez
-- Carlos Rodríguez
-- Departamentos
-- Desarrollo
-- Juan García
-- María López
-- Pedro Sánchez
-- Recursos Humanos
-- Ventas