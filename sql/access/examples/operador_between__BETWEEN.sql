-- Operador BETWEEN en Microsoft Access
-- Busca empleados con salario entre 3700 y 4200

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Salario BETWEEN 3700 AND 4200;

-- Output:
-- ID | Nombre           | Departamento_ID | Salario
-- ---|-----------------|-----------------|--------
-- 2  | María López      | 2               | 4200
-- 3  | Carlos Rodríguez | 1               | 3800
-- 5  | Pedro Sánchez   | 2               | 3900