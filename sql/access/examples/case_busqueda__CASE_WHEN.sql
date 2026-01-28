"""
Objetivo: case busqueda
Referencia: CASE_WHEN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT nombre, CASE edad WHEN 25 THEN 'Joven' WHEN 30 THEN 'Adulto' ELSE 'Otro' END AS categoria FROM empleados;

/*output
nombre_empleado | años
-----------------|------
Juan            | 30
María           | 28
Carlos          | 35
*/