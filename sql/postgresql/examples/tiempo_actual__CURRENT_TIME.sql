/*
 * Objetivo: Obtener la hora actual
 * Referencia: CURRENT_TIME
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Obtener hora actual
SELECT CURRENT_TIME as ahora;

-- Con zona horaria
SELECT CURRENT_TIME AT TIME ZONE 'UTC' as ahora_utc;

-- Crear tabla con hora
CREATE TABLE IF NOT EXISTS eventos (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(100),
    hora_inicio TIME DEFAULT CURRENT_TIME
);

-- Insertar evento
INSERT INTO eventos (descripcion) VALUES ('Reunión');

-- Consultar con hora
SELECT * FROM eventos;

-- Comparar horas
SELECT CURRENT_TIME, CURRENT_TIME > '12:00'::TIME as es_tarde;

/*
Output esperado:
    ahora
-----------
 14:30:45.123456
*/
