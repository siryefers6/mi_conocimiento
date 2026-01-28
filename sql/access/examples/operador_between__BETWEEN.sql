-- Operador BETWEEN en Microsoft Access
-- Busca empleados con salario entre 3700 y 4200

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Salario BETWEEN 3700 AND 4200;

