/*
 * Objetivo: Vaciar completamente una tabla de forma rápida
 * Referencia: TRUNCATE
 * Tipo: DML (Data Manipulation Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    mensaje TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO logs (mensaje)
VALUES
    ('Error en módulo A'),
    ('Advertencia en módulo B'),
    ('Info del sistema');

-- Ver datos
SELECT COUNT(*) as total FROM logs;

-- TRUNCATE (elimina todas las filas rápidamente)
TRUNCATE TABLE logs;

-- Ver resultado
SELECT COUNT(*) as total FROM logs;

-- TRUNCATE con reinicio de secuencia
TRUNCATE TABLE logs RESTART IDENTITY;

/*
Output esperado (antes):
 total
-------
     3

Output esperado (después):
 total
-------
     0
*/
