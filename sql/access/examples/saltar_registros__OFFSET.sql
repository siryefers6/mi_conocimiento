"""
Objetivo: saltar registros
Referencia: OFFSET
Tipo: clausula
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE id NOT IN (SELECT TOP 5 id FROM empleados ORDER BY id);

/*output
nombre | edad
--------|------
Carlos | 35
Ana    | 32
*/