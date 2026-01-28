"""
Objetivo: nullif
Referencia: NULLIF
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT IIf(campo = 'valor', Null, campo) FROM tabla;

/*output
Operación completada correctamente
*/