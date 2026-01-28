"""
Objetivo: primer no nulo
Referencia: NZ
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT Nz(campo, 'default') FROM tabla;

/*output
nombre | telefono
--------|----------
Juan   | 555-1234
María  | (sin datos)
Carlos | 555-5678
*/