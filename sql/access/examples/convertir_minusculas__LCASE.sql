"""
Objetivo: convertir minusculas
Referencia: LCASE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT LCase(nombre) FROM empleados;

/*output
nombre_empleado | años
-----------------|------
Juan            | 30
María           | 28
Carlos          | 35
*/