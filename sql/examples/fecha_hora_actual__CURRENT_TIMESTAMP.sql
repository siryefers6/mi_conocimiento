/*
 * Objetivo: Obtener la fecha y hora actual (timestamp)
 * Referencia: CURRENT_TIMESTAMP
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Obtener timestamp actual
SELECT CURRENT_TIMESTAMP as ahora;

-- Crear tabla con timestamp
CREATE TABLE IF NOT EXISTS cambios (
    id SERIAL PRIMARY KEY,
    tabla VARCHAR(50),
    accion VARCHAR(20),
    momento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar registros
INSERT INTO cambios (tabla, accion) VALUES ('usuarios', 'INSERT');
INSERT INTO cambios (tabla, accion) VALUES ('productos', 'UPDATE');

-- Ver cambios con timestamp
SELECT * FROM cambios;

-- Diferencia de tiempo
SELECT 
    CURRENT_TIMESTAMP as ahora,
    CURRENT_TIMESTAMP - INTERVAL '1 day' as hace_un_dia,
    CURRENT_TIMESTAMP + INTERVAL '1 hour' as en_una_hora;

/*
Output esperado:
         ahora
------------------------
 2024-01-27 14:30:45.123
*/
