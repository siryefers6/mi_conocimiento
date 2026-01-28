"""
Objetivo: Unir tablas mostrando solo coincidencias
Referencia: INNER_JOIN
Tipo: join
Nivel: intermedio
"""

SELECT e.Nombre, d.Nombre AS Departamento, e.Salario
FROM Empleados e 
INNER JOIN Departamentos d ON e.Departamento_ID = d.ID;
