-- Operador OR en Microsoft Access
-- Busca empleados de Desarrollo o Recursos Humanos

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID = 1 OR Departamento_ID = 3;

