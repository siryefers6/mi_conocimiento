"""
Objetivo: concatenar strings
Referencia: CONCAT
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT nombre & ' ' & apellido AS nombre_completo FROM empleados;

/*output
nombre_completo
-----------------
Juan García
María López
Carlos Rodríguez
*/