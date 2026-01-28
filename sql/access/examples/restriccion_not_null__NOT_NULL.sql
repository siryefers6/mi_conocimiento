"""
Objetivo: restriccion not null
Referencia: NOT_NULL
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50) NOT NULL
);

