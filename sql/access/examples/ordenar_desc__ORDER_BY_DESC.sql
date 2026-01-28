-- Ordenar descendente en Microsoft Access
-- Ordena empleados por salario de mayor a menor

SELECT ID, Nombre, Departamento_ID, Salario, Fecha_Contratacion
FROM Empleados
ORDER BY Salario DESC;

-- Output:
-- ID | Nombre           | Departamento_ID | Salario | Fecha_Contratacion
-- ---|------------------|-----------------|---------|--------------------
-- 4  | Ana Martínez     | 3               | 4500    | 2018-11-05
-- 2  | María López      | 2               | 4200    | 2019-07-22
-- 3  | Carlos Rodríguez | 1               | 3800    | 2021-01-10
-- 5  | Pedro Sánchez    | 2               | 3900    | 2022-05-18
-- 1  | Juan García      | 1               | 3500    | 2020-03-15