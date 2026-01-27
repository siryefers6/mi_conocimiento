-- RIGHT JOIN en Microsoft Access
SELECT e.nombre, d.nombre_dept FROM empleados e RIGHT JOIN departamentos d ON e.dept_id = d.id;