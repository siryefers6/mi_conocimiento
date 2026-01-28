"""
Objetivo: operador like
Referencia: LIKE
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE nombre LIKE 'J*';

/*output
nombre | edad
--------|------
Juan   | 30
*/