"""
Objetivo: operador or
Referencia: OR
Tipo: operador
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE edad > 25 OR departamento = 'IT';

/*output
nombre | edad | departamento
--------|------|---------------
Juan   | 30   | Ventas
Carlos | 35   | RH
*/