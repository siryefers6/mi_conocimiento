-- LEN en Microsoft Access
-- Obtiene la longitud del nombre de cada empleado

SELECT Nombre, LEN(Nombre) AS Longitud_Nombre
FROM Empleados;

-- Output:
-- Nombre           | Longitud_Nombre
-- -------------- | ---------------
-- Juan García     | 11
-- María López     | 12
-- Carlos Rodríguez | 16
-- Ana Martínez    | 12
-- Pedro Sánchez    | 13