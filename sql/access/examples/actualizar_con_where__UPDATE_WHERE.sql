"""
Objetivo: actualizar con where
Referencia: UPDATE_WHERE
Tipo: funcion
Nivel: basico
"""

-- transformacion
UPDATE empleados SET edad = edad + 1 WHERE edad < 30;

/*output
nombre | edad
--------|------
Carlos | 35
Juan   | 30
*/