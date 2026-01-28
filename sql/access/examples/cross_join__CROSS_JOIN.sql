"""
Objetivo: cross join
Referencia: CROSS_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT e.nombre, d.nombre_dept FROM empleados e, departamentos d;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/