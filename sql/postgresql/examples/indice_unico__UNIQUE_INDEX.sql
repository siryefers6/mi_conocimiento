/*
 * Objetivo: Crear índice con restricción de unicidad
 * Referencia: UNIQUE INDEX
 * Tipo: optimización
 * Nivel: intermedio
 */

-- Crear tabla
CREATE TABLE IF NOT EXISTS usuarios_unicos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Crear índice único
CREATE UNIQUE INDEX idx_email_unico ON usuarios_unicos(email);

-- Ahora no se pueden insertar emails duplicados
INSERT INTO usuarios_unicos (nombre, email)
VALUES ('Juan', 'juan@email.com');

-- Esta inserción fallará (email duplicado)
-- INSERT INTO usuarios_unicos (nombre, email)
-- VALUES ('Juan2', 'juan@email.com');

-- Ver índices
\di usuarios_unicos

/*
UNIQUE INDEX:
- Garantiza unicidad en la columna
- Acepta un NULL (generalmente)
- Más rápido para búsquedas que sin índice
*/
