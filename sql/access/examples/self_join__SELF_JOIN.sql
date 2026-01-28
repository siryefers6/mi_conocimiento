"""
Objetivo: self join
Referencia: SELF_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT e1.nombre AS empleado, e2.nombre AS jefe FROM empleados e1 INNER JOIN empleados e2 ON e1.jefe_id = e2.id;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/