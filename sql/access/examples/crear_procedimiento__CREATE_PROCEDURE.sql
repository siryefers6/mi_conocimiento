"""
Objetivo: crear procedimiento almacenado
Referencia: CREATE_PROCEDURE
Tipo: keyword
Nivel: basico
"""

-- transformacion
CREATE PROCEDURE ActualizarEdad
AS
UPDATE empleados SET edad = YEAR(NOW()) - YEAR(fecha_nac);

/*output
Procedimiento creado: ActualizarEdad
Estado: Listo para ejecutar
*/