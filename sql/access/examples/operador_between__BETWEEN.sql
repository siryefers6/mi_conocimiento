"""
Objetivo: operador between
Referencia: BETWEEN
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE edad BETWEEN 25 AND 35;

/*output
nombre | edad
--------|------
Juan   | 30
María  | 28
*/