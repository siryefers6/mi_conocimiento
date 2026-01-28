"""
Objetivo: clave foranea
Referencia: FOREIGN_KEY
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departamentos(id)
);

