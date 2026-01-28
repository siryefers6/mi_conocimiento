"""
Objetivo: union
Referencia: UNION
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT nombre FROM empleados UNION SELECT nombre FROM ex_empleados;

/*output
nombre
--------
Juan
María
Carlos
Pedro
*/