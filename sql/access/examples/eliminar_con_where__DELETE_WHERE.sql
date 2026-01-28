"""
Objetivo: eliminar con where
Referencia: DELETE_WHERE
Tipo: funcion
Nivel: basico
"""

-- transformacion
DELETE FROM empleados WHERE edad > 60;

/*output
nombre | edad
--------|------
Carlos | 35
Juan   | 30
*/