/*
 * Objetivo: Cambiar el nombre de una columna
 * Referencia: RENAME COLUMN
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS articulos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    desc TEXT,
    precio DECIMAL(10, 2)
);

-- Renombrar columna desc a descripcion
ALTER TABLE articulos RENAME COLUMN desc TO descripcion;

-- Renombrar columna titulo a nombre_articulo
ALTER TABLE articulos RENAME COLUMN titulo TO nombre_articulo;

-- Ver estructura actualizada
\d articulos

/*
Output esperado:
Table "public.articulos"
 Column | Type | Modifiers
--------------------|---------|---------------------------
 id | integer | not null default nextval(...)
 nombre_articulo | character varying(200) |
 descripcion | text |
 precio | numeric(10,2) |
*/
