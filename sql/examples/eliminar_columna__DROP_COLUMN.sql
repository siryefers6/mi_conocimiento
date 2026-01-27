/*
 * Objetivo: Eliminar una columna de una tabla
 * Referencia: DROP COLUMN
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad INT,
    descripcion TEXT
);

-- Eliminar columna simple
ALTER TABLE personas DROP COLUMN descripcion;

-- Eliminar columna con cascada (si hay referencias)
ALTER TABLE personas DROP COLUMN edad CASCADE;

-- Ver estructura actualizada
\d personas

/*
Output esperado:
Table "public.personas"
 Column | Type | Modifiers
--------|------|---------------------------
 id | integer | not null default nextval(...)
 nombre | character varying(100) |
 apellido | character varying(100) |
*/
