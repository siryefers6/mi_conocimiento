/*
 * Objetivo: Crear un índice para optimizar búsquedas
 * Referencia: CREATE INDEX
 * Tipo: DDL (Data Definition Language)
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200),
    precio DECIMAL(10, 2),
    categoria VARCHAR(100)
);

-- Crear índice simple en una columna
CREATE INDEX idx_productos_nombre ON productos(nombre);

-- Crear índice con nombre descriptivo
CREATE INDEX idx_productos_categoria ON productos(categoria);

-- Crear índice único (también es constraint)
CREATE UNIQUE INDEX idx_email ON usuarios(email);

-- Listar índices
\di

/*
Output esperado:
Schema | Name | Type | Table | Size | ...
--------|------|------|-------|------|
 public | idx_productos_nombre | index | productos | 8192 bytes | ...
*/
