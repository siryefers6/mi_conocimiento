-- Operador LIKE en Microsoft Access
-- Busca empleados cuyo nombre comienza con 'M'

SELECT ID, Nombre, Departamento_ID, Salario 
FROM Empleados 
WHERE Nombre LIKE 'M*';

-- Output:
-- ID | Nombre      | Departamento_ID | Salario
-- ---|-------------|-----------------|--------
-- 2  | María López | 2               | 4200