"""
Objetivo: sumar dias
Referencia: DATEADD
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT DateAdd('d', 7, fecha) AS nueva_fecha FROM tabla;

/*output
fecha_actual
-----------
2025-01-28
*/