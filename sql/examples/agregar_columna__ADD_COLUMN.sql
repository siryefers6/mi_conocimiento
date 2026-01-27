/*
 * Objetivo: Agregar una nueva columna a una tabla existente
 * Referencia: ADD COLUMN
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Agregar columna simple
ALTER TABLE estudiantes ADD COLUMN matricula VARCHAR(20);

-- Agregar columna con tipo de dato
ALTER TABLE estudiantes ADD COLUMN edad INT;

-- Agregar columna con restricción NOT NULL y valor por defecto
ALTER TABLE estudiantes ADD COLUMN activo BOOLEAN DEFAULT true;

-- Agregar columna con restricción UNIQUE
ALTER TABLE estudiantes ADD COLUMN email VARCHAR(100) UNIQUE;

-- Ver estructura de tabla
\d estudiantes

/*
Output esperado:
Table "public.estudiantes"
 Column | Type | Modifiers
----------|----------|---------------------------
 id | integer | not null default nextval(...)
 nombre | character varying(100) |
 matricula | character varying(20) |
 edad | integer |
 activo | boolean | default true
 email | character varying(100) | unique
*/
