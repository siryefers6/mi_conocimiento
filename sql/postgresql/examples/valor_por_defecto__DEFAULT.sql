/*
 * Objetivo: Asignar valor predeterminado a una columna
 * Referencia: DEFAULT
 * Tipo: constraint DDL
 * Nivel: básico
 */

-- DEFAULT con valor literal
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    pais VARCHAR(50) DEFAULT 'España',
    activo BOOLEAN DEFAULT true
);

-- DEFAULT con función
CREATE TABLE IF NOT EXISTS articulos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DEFAULT con expresión
CREATE TABLE IF NOT EXISTS ordenes (
    id SERIAL PRIMARY KEY,
    numero INT DEFAULT nextval('seq_ordenes'),
    estado VARCHAR(50) DEFAULT 'PENDIENTE',
    creado_en TIMESTAMP DEFAULT now()
);

-- Cambiar valor DEFAULT
ALTER TABLE usuarios ALTER COLUMN pais SET DEFAULT 'México';

-- Remover DEFAULT
ALTER TABLE usuarios ALTER COLUMN pais DROP DEFAULT;

-- Ver estructura
\d usuarios

/*
Output esperado:
Column | Type | Modifiers
--------|------|---------------------------
 id | integer | not null default nextval(...)
 nombre | character varying(100) |
 pais | character varying(50) | default 'México'::character varying
 activo | boolean | default true
*/
