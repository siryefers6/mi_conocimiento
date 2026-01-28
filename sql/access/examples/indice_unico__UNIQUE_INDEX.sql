"""
Objetivo: indice unico
Referencia: UNIQUE_INDEX
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE UNIQUE INDEX idx_email ON empleados (email);

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/