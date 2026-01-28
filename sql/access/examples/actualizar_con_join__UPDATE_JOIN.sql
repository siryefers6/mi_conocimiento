"""
Objetivo: actualizar con join
Referencia: UPDATE_JOIN
Tipo: funcion
Nivel: basico
"""

-- transformacion
UPDATE empleados INNER JOIN departamentos ON empleados.dept_id = departamentos.id
SET empleados.salario = empleados.salario * 1.1;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/