"""
Objetivo: otorgar permisos a usuario
Referencia: GRANT
Tipo: keyword
Nivel: basico
"""

-- transformacion
GRANT SELECT, INSERT ON empleados TO juan;

/*output
Permisos otorgados:
Usuario: juan
Tabla: empleados
Permisos: SELECT, INSERT
*/