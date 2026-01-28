"""
Objetivo: diferencia fechas
Referencia: DATEDIFF
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT DateDiff('d', fecha1, fecha2) AS dias_diferencia FROM tabla;

/*output
fecha_actual
-----------
2025-01-28
*/