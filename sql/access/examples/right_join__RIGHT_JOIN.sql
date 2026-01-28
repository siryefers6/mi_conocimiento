"""
Objetivo: right join
Referencia: RIGHT_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT e.nombre, d.nombre_dept FROM empleados e RIGHT JOIN departamentos d ON e.dept_id = d.id;

