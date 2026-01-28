"""
Objetivo: ordenar desc
Referencia: ORDER_BY_DESC
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados ORDER BY edad DESC;

/*output
nombre | edad | departamento
--------|------|---------------
Juan   | 30   | Ventas
Carlos | 35   | RH
*/