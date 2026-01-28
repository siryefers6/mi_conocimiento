"""
Objetivo: Combinar resultados de múltiples consultas
Referencia: UNION
Tipo: select
Nivel: intermedio
"""

SELECT Nombre FROM Empleados
UNION
SELECT Nombre FROM Departamentos;
