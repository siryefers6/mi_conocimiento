"""
Objetivo: agregar columna
Referencia: ADD_COLUMN
Tipo: funcion
Nivel: basico
"""

-- transformacion
ALTER TABLE empleados ADD COLUMN departamento TEXT(30);

/*output
Columna añadida: telefono
Tipo: TEXT
*/