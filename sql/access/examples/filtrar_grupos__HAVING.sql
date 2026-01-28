"""
Objetivo: filtrar grupos
Referencia: HAVING
Tipo: clausula
Nivel: basico
"""

-- transformacion
SELECT departamento, COUNT(*) FROM empleados GROUP BY departamento HAVING COUNT(*) > 5;

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/