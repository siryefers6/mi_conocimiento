"""
Objetivo: subconsulta from
Referencia: SUBQUERY_FROM
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT avg_edad FROM (SELECT AVG(edad) AS avg_edad FROM empleados) AS sub;

