"""
Objetivo: vista filtrada
Referencia: VIEW_WHERE
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE VIEW vista_adultos AS SELECT * FROM empleados WHERE edad > 18;

/*output
nombre | edad
--------|------
Carlos | 35
Juan   | 30
*/