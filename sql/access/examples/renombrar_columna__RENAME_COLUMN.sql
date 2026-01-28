"""
Objetivo: renombrar columna
Referencia: RENAME_COLUMN
Tipo: funcion
Nivel: basico
"""

-- transformacion
ALTER TABLE empleados ADD COLUMN nombre_completo TEXT(50);
ALTER TABLE empleados DROP COLUMN nombre;

/*output
Columna renombrada: edad_empleado -> edad
*/