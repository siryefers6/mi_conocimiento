"""
Objetivo: restriccion check
Referencia: CHECK
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    edad INTEGER
);

/*output
Restricción creada
Campo: edad
Condición: edad >= 18
*/