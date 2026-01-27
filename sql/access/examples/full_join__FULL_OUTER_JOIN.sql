-- FULL OUTER JOIN en Microsoft Access
-- Nota: Access no soporta FULL OUTER JOIN; usar LEFT JOIN UNION RIGHT JOIN.
SELECT e.nombre, d.nombre_dept FROM empleados e LEFT JOIN departamentos d ON e.dept_id = d.id
UNION
SELECT e.nombre, d.nombre_dept FROM empleados e RIGHT JOIN departamentos d ON e.dept_id = d.id;