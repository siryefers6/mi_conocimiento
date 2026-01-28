"""
Objetivo: Unir tablas conservando todos los registros de la izquierda
Referencia: LEFT_JOIN
Tipo: join
Nivel: intermedio
"""

SELECT e.Nombre, d.Nombre AS Departamento
FROM Empleados e 
LEFT JOIN Departamentos d ON e.Departamento_ID = d.ID;
