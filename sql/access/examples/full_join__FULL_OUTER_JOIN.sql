"""
Objetivo: full join
Referencia: FULL_OUTER_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT e.nombre, d.nombre_dept FROM empleados e LEFT JOIN departamentos d ON e.dept_id = d.id
UNION
SELECT e.nombre, d.nombre_dept FROM empleados e RIGHT JOIN departamentos d ON e.dept_id = d.id;

