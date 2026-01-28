"""
Objetivo: reemplazar texto
Referencia: REPLACE
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT Replace(nombre, 'a', 'o') FROM empleados;

/*output
nombre_reemplazado
-------------------
Pedro García
Paula López
Carlos Rodríguez
*/