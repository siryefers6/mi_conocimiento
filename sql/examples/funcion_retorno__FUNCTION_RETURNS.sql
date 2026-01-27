/*
 * Objetivo: Crear función con tipo de retorno especificado
 * Referencia: RETURNS
 * Tipo: PL/pgSQL
 * Nivel: intermedio
 */

-- Función que retorna INT
CREATE OR REPLACE FUNCTION contar_registros(p_tabla VARCHAR)
RETURNS INT AS $$
DECLARE
    v_count INT;
BEGIN
    EXECUTE 'SELECT COUNT(*) FROM ' || p_tabla INTO v_count;
    RETURN v_count;
END;
$$ LANGUAGE plpgsql;

-- Función que retorna BOOLEAN
CREATE OR REPLACE FUNCTION existe_usuario(p_email VARCHAR)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS(SELECT 1 FROM usuarios WHERE email = p_email);
END;
$$ LANGUAGE plpgsql;

-- Función que retorna RECORD
CREATE OR REPLACE FUNCTION obtener_estadisticas()
RETURNS TABLE(tabla VARCHAR, registros INT) AS $$
BEGIN
    RETURN QUERY
    SELECT 'usuarios'::VARCHAR, COUNT(*)::INT FROM usuarios
    UNION ALL
    SELECT 'productos'::VARCHAR, COUNT(*)::INT FROM productos;
END;
$$ LANGUAGE plpgsql;

-- Usar las funciones
-- SELECT contar_registros('usuarios');
-- SELECT existe_usuario('juan@email.com');
-- SELECT * FROM obtener_estadisticas();

/*
Las funciones con RETURNS especifican el tipo de dato que devuelven.
Puede ser escalares (INT, VARCHAR, BOOLEAN) o complejos (TABLE, RECORD).
*/
