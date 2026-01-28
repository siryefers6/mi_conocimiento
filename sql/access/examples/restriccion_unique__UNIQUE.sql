"""
Objetivo: restriccion unique
Referencia: UNIQUE
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    email TEXT(50) UNIQUE
);

/*output
Restricción creada
Campo: email
Tipo: UNIQUE
*/