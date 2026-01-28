"""
Objetivo: insertar desde select
Referencia: INSERT_SELECT
Tipo: funcion
Nivel: basico
"""

-- transformacion
INSERT INTO empleados_backup (id, nombre, edad)
SELECT id, nombre, edad FROM empleados;

