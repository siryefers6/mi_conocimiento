"""
Objetivo: remover espacios
Referencia: TRIM
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT Trim(nombre) FROM empleados;

/*output
nombre_limpio
--------------
Juan
María
Carlos
*/