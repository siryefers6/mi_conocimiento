"""
Objetivo: case simple
Referencia: CASE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT nombre, CASE WHEN edad > 30 THEN 'Mayor' ELSE 'Menor' END AS categoria FROM empleados;

/*output
nombre_empleado | años
-----------------|------
Juan            | 30
María           | 28
Carlos          | 35
*/