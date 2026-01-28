"""
Objetivo: cambiar tipo de columna
Referencia: ALTER_COLUMN_TYPE
Tipo: keyword
Nivel: basico
"""

-- transformacion
ALTER TABLE empleados MODIFY COLUMN edad TEXT;

/*output
Cambio de tipo completado
Tabla: empleados
Columna: edad
Nuevo tipo: TEXT
*/