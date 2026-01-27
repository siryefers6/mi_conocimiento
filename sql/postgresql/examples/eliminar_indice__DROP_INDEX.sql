/*
 * Objetivo: Eliminar un índice
 * Referencia: DROP INDEX
 * Tipo: optimización
 * Nivel: básico
 */

-- Crear tabla y índice
CREATE TABLE IF NOT EXISTS articulos_temp (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50)
);

CREATE INDEX idx_categoria ON articulos_temp(categoria);

-- Ver índices
\di articulos_temp

-- Eliminar índice
DROP INDEX idx_categoria;

-- Eliminar solo si existe (no da error si no existe)
DROP INDEX IF EXISTS idx_no_existe;

-- Eliminar índice y tablas que lo usan
DROP INDEX IF EXISTS idx_categoria CASCADE;

/*
Cuándo eliminar índices:
- Ya no se usan en consultas
- Ralentizan inserciones/actualizaciones
- Ocupan demasiado espacio
*/
