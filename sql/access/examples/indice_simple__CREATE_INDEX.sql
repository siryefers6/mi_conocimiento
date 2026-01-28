"""
Objetivo: indice simple
Referencia: CREATE_INDEX
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE INDEX idx_nombre ON empleados (nombre);

/*output
nombre | departamento
--------|---------------
Juan   | Ventas
María  | TI
*/