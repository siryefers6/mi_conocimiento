/*
 * Objetivo: Cambiar el tipo de dato de una columna
 * Referencia: ALTER COLUMN TYPE
 * Tipo: DDL (Data Definition Language)
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS datos (
    id SERIAL PRIMARY KEY,
    valor VARCHAR(50),
    cantidad VARCHAR(100)
);

-- Cambiar tipo de VARCHAR a INTEGER
ALTER TABLE datos ALTER COLUMN valor TYPE INTEGER USING valor::INTEGER;

-- Cambiar tipo de VARCHAR a DECIMAL
ALTER TABLE datos ALTER COLUMN cantidad TYPE DECIMAL(10,2) USING cantidad::DECIMAL;

-- Cambiar tipo a TIMESTAMP
ALTER TABLE datos ADD COLUMN fecha_texto VARCHAR(50);
ALTER TABLE datos ALTER COLUMN fecha_texto TYPE TIMESTAMP USING fecha_texto::TIMESTAMP;

-- Ver estructura actualizada
\d datos

/*
Output esperado:
Table "public.datos"
 Column | Type | Modifiers
--------------------|---------|---------------------------
 id | integer | not null default nextval(...)
 valor | integer |
 cantidad | numeric(10,2) |
 fecha_texto | timestamp without time zone |
*/
