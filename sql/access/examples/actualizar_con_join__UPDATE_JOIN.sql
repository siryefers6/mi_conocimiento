-- Actualizar con JOIN en Microsoft Access
UPDATE empleados INNER JOIN departamentos ON empleados.dept_id = departamentos.id
SET empleados.salario = empleados.salario * 1.1;