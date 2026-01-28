"""
Objetivo: inner join
Referencia: INNER_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT e.nombre, d.nombre_dept FROM empleados e INNER JOIN departamentos d ON e.dept_id = d.id;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/