"""
Objetivo: except
Referencia: EXCEPT
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT e.nombre FROM empleados e LEFT JOIN ex_empleados ex ON e.nombre = ex.nombre WHERE ex.nombre IS NULL;

/*output
nombre
--------
Pedro
Ana
*/