"""
Objetivo: verificar existe
Referencia: EXISTS
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados e WHERE EXISTS (SELECT 1 FROM departamentos d WHERE d.id = e.dept_id);

/*output
nombre | edad
--------|------
Juan   | 30
María  | 28
Carlos | 35
*/