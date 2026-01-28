"""
Objetivo: intersect
Referencia: INTERSECT
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT DISTINCT e.nombre FROM empleados e INNER JOIN ex_empleados ex ON e.nombre = ex.nombre;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/