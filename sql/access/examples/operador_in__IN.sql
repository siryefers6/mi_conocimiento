"""
Objetivo: operador in
Referencia: IN
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE departamento IN ('IT', 'HR');

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/