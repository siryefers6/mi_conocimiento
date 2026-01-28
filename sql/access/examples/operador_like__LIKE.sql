-- Operador LIKE en Microsoft Access
-- Busca empleados cuyo nombre comienza con 'M'

SELECT ID, Nombre, Departamento_ID, Salario 
FROM Empleados 
WHERE Nombre LIKE 'M*';

