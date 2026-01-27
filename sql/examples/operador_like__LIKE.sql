/*
 * Objetivo: Buscar filas con patrones de texto
 * Referencia: LIKE
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Insertar datos de prueba
INSERT INTO usuarios (nombre, email)
VALUES
    ('Juan García', 'juan@gmail.com'),
    ('María López', 'maria@hotmail.com'),
    ('Juan Pérez', 'jp@gmail.com'),
    ('Carlos García', 'carlos@yahoo.com'),
    ('Ana García', 'ana.garcia@gmail.com');

-- % representa cualquier secuencia de caracteres
SELECT * FROM usuarios WHERE nombre LIKE 'Juan%';

-- _ representa un carácter exacto
SELECT * FROM usuarios WHERE nombre LIKE '_uan%';

-- LIKE con patrón al principio
SELECT * FROM usuarios WHERE email LIKE '%@gmail.com';

-- LIKE para búsqueda en medio
SELECT * FROM usuarios WHERE nombre LIKE '%García%';

-- ILIKE (case insensitive)
SELECT * FROM usuarios WHERE nombre ILIKE 'juan%';

/*
Output esperado:
 id |     nombre     |      email
----|----------------|-------------------
  1 | Juan García | juan@gmail.com
  3 | Juan Pérez | jp@gmail.com
*/
