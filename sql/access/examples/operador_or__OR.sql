-- Operador OR en Microsoft Access
-- Busca empleados de Desarrollo o Recursos Humanos

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID = 1 OR Departamento_ID = 3;

-- Output:
-- ID | Nombre           | Departamento_ID | Salario
-- ---|-----------------|-----------------|--------
-- 1  | Juan García     | 1               | 3500
-- 3  | Carlos Rodríguez | 1               | 3800
-- 4  | Ana Martínez    | 3               | 4500