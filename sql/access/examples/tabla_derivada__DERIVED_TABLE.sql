"""
Objetivo: tabla derivada
Referencia: DERIVED_TABLE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT * FROM (SELECT nombre, edad FROM empleados) AS sub;

/*output
edad | nombre_count
------|-------------
30   | 2
28   | 1
35   | 1
*/