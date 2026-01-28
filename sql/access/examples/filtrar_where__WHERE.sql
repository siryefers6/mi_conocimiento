-- Filtrar con WHERE en Microsoft Access
-- Obtiene empleados con salario mayor a 3700

SELECT ID, Nombre, Departamento_ID, Salario 
FROM Empleados 
WHERE Salario > 3700;

-- Output:
-- ID | Nombre           | Departamento_ID | Salario
-- ---|-----------------|-----------------|--------
-- 2  | María López      | 2               | 4200
-- 3  | Carlos Rodríguez | 1               | 3800
-- 4  | Ana Martínez    | 3               | 4500
-- 5  | Pedro Sánchez   | 2               | 3900