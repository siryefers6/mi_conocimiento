"""
Objetivo: revocar permisos a usuario
Referencia: REVOKE
Tipo: keyword
Nivel: basico
"""

-- transformacion
REVOKE DELETE ON empleados FROM juan;

/*output
Permisos revocados:
Usuario: juan
Tabla: empleados
Permiso: DELETE
*/