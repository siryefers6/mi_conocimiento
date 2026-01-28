"""
Objetivo: clave primaria
Referencia: PRIMARY_KEY
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50)
);

/*output
Restricción creada
Campo: id
Tipo: PRIMARY KEY
*/