-- DISTINCT en Microsoft Access
-- Obtiene los departamentos únicos sin repeticiones

SELECT DISTINCT Departamento_ID
FROM Empleados
ORDER BY Departamento_ID;

-- Output:
-- Departamento_ID
-- ---------------
-- 1
-- 2
-- 3