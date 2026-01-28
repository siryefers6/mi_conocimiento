"""
Objetivo: agrupar datos
Referencia: GROUP_BY
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT departamento, COUNT(*) FROM empleados GROUP BY departamento;

/*output
departamento | cantidad
-----------|---------
Ventas     | 3
TI         | 2
RH         | 1
*/