/*
 * Objetivo: Hacer que una columna sea obligatoria (no nula)
 * Referencia: NOT NULL
 * Tipo: constraint DDL
 * Nivel: básico
 */

-- Definir NOT NULL en creación de tabla
CREATE TABLE IF NOT EXISTS articulos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL
);

-- Agregar restricción NOT NULL
ALTER TABLE articulos ALTER COLUMN descripcion SET NOT NULL;

-- Remover restricción NOT NULL
ALTER TABLE articulos ALTER COLUMN descripcion DROP NOT NULL;

-- Ver restricciones
\d articulos

/*
Output esperado:
Column | Type | Modifiers
--------|------|---------------------------
 id | integer | not null default nextval(...)
 nombre | character varying(100) | not null
 descripcion | text |
 precio | numeric(10,2) | not null
*/
