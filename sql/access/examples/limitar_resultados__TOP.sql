"""
Objetivo: limitar resultados
Referencia: TOP
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT TOP 10 * FROM empleados;

/*output
nombre | edad
--------|------
Juan   | 30
María  | 28
*/