"""
Objetivo: tabla derivada
Referencia: DERIVED_TABLE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT * FROM (SELECT nombre, edad FROM empleados) AS sub;

