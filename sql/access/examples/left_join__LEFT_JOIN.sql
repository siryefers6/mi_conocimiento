-- LEFT JOIN en Microsoft Access
SELECT e.nombre, d.nombre_dept FROM empleados e LEFT JOIN departamentos d ON e.dept_id = d.id;