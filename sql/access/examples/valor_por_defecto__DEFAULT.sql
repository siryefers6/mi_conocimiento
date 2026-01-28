"""
Objetivo: valor por defecto
Referencia: DEFAULT
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50),
    activo YESNO DEFAULT YES
);

