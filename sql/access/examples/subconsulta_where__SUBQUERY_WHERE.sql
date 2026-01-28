-- Subconsulta en WHERE en Microsoft Access
-- Busca empleados con salario mayor al promedio

SELECT ID, Nombre, Salario
FROM Empleados
WHERE Salario > (SELECT AVG(Salario) FROM Empleados);

-- Output:
-- ID | Nombre        | Salario
-- ---|---------------|--------
-- 2  | María López   | 4200
-- 4  | Ana Martínez  | 4500