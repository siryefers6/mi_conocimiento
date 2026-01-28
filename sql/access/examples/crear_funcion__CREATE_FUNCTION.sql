"""
Objetivo: crear función personalizada
Referencia: CREATE_FUNCTION
Tipo: keyword
Nivel: basico
"""

-- transformacion
CREATE FUNCTION ObtenerEdad(fecha_nac DATE) RETURNS INT AS
BEGIN
    RETURN YEAR(NOW()) - YEAR(fecha_nac);
END;

