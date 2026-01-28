"""
Objetivo: subconsulta where
Referencia: SUBQUERY_WHERE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE edad > (SELECT AVG(edad) FROM empleados);

/*output
nombre | edad
--------|------
Carlos | 35
Juan   | 30
*/