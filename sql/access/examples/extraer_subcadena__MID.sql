"""
Objetivo: extraer subcadena
Referencia: MID
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT Mid(nombre, 1, 3) FROM empleados;

/*output
primeras_3_letras
------------------
Jua
Mar
Car
*/