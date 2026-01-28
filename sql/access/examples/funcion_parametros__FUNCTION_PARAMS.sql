"""
Objetivo: definir función con parámetros
Referencia: FUNCTION_PARAMS
Tipo: keyword
Nivel: basico
"""

-- transformacion
CREATE FUNCTION SumarEdades(edad1 INT, edad2 INT) RETURNS INT
AS
BEGIN
    RETURN edad1 + edad2;
END;

