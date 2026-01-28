-- Operador IN en Microsoft Access
-- Busca empleados de los departamentos 1 (Desarrollo) o 2 (Ventas)

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID IN (1, 2);

-- Output:
-- ID | Nombre           | Departamento_ID | Salario
-- ---|-----------------|-----------------|--------
-- 1  | Juan García     | 1               | 3500
-- 2  | María López      | 2               | 4200
-- 3  | Carlos Rodríguez | 1               | 3800
-- 5  | Pedro Sánchez   | 2               | 3900