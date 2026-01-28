-- Operador AND en Microsoft Access
-- Busca empleados del departamento 1 con salario mayor a 3600

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID = 1 AND Salario > 3600;

