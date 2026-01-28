"""
Objetivo: Agrupar y contar registros por categorías
Referencia: GROUP_BY
Tipo: select
Nivel: intermedio
"""

SELECT d.Nombre AS Departamento, COUNT(e.ID) AS Total_Empleados
FROM Empleados e
JOIN Departamentos d ON e.Departamento_ID = d.ID
GROUP BY d.Nombre;
