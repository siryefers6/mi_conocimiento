/*
 * Objetivo: Modificar estructura de una tabla existente
 * Referencia: ALTER TABLE
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Agregar nueva columna
ALTER TABLE clientes ADD COLUMN email VARCHAR(100);

-- Agregar columna con valor por defecto
ALTER TABLE clientes ADD COLUMN fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Cambiar nombre de tabla
ALTER TABLE clientes RENAME TO customers;

-- Renombrar tabla nuevamente para continuar
ALTER TABLE customers RENAME TO clientes;

-- Cambiar propiedades de columna
ALTER TABLE clientes ALTER COLUMN nombre SET NOT NULL;

-- Describir estructura de tabla
\d clientes

/*
Output esperado:
Table "public.clientes"
 Column | Type | Modifiers
---------|---------|---------------------------
 id | integer | not null default nextval(...)
 nombre | character varying(100) | not null
 email | character varying(100) |
 fecha_registro | timestamp | default CURRENT_TIMESTAMP
*/
