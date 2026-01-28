"""
Objetivo: definir tipo de retorno en función
Referencia: FUNCTION_RETURNS
Tipo: keyword
Nivel: basico
"""

-- transformacion
CREATE FUNCTION ObtenerNombre(id INT) RETURNS VARCHAR(50)
AS
BEGIN
    RETURN (SELECT nombre FROM empleados WHERE id = id);
END;

