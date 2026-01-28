"""
Objetivo: operador and
Referencia: AND
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE edad > 25 AND departamento = 'IT';

/*output
nombre | edad | departamento
--------|------|---------------
Carlos | 35   | RH
*/