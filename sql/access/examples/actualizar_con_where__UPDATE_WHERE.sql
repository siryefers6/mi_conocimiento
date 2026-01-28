-- Actualizar con WHERE en Microsoft Access
-- Aumenta el salario en 5% a los empleados del departamento 1

UPDATE Empleados 
SET Salario = Salario * 1.05 
WHERE Departamento_ID = 1;

-- Output:
-- 2 registros actualizados
-- Juan García: 3500 -> 3675
-- Carlos Rodríguez: 3800 -> 3990