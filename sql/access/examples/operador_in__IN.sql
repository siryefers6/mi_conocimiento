-- Operador IN en Microsoft Access
-- Busca empleados de los departamentos 1 (Desarrollo) o 2 (Ventas)

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID IN (1, 2);

