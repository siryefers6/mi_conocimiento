/*
 * Objetivo: Crear un procedimiento almacenado
 * Referencia: CREATE PROCEDURE
 * Tipo: PL/pgSQL
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS eventos_log (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(200),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear procedimiento simple
CREATE OR REPLACE PROCEDURE registrar_evento(p_descripcion VARCHAR)
AS $$
BEGIN
    INSERT INTO eventos_log (descripcion) VALUES (p_descripcion);
    COMMIT;
END;
$$ LANGUAGE plpgsql;

-- Ejecutar procedimiento
CALL registrar_evento('Evento 1');
CALL registrar_evento('Evento 2');

-- Ver logs
SELECT * FROM eventos_log;

-- Procedimiento con múltiples operaciones
CREATE OR REPLACE PROCEDURE inicializar_sistema()
AS $$
BEGIN
    DELETE FROM eventos_log;
    INSERT INTO eventos_log (descripcion) VALUES ('Sistema inicializado');
    COMMIT;
END;
$$ LANGUAGE plpgsql;

-- Ejecutar
-- CALL inicializar_sistema();

/*
Output esperado:
 id |     descripcion     |        fecha
----|---------------------|------------------------
  1 | Evento 1 | 2024-01-27 14:30:45.123
  2 | Evento 2 | 2024-01-27 14:30:46.456
*/
