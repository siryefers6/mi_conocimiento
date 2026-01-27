/*
 * Objetivo: Saltar filas iniciales del resultado
 * Referencia: OFFSET
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS articulos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    precio DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO articulos (titulo, precio)
VALUES
    ('Producto 1', 10),
    ('Producto 2', 20),
    ('Producto 3', 30),
    ('Producto 4', 40),
    ('Producto 5', 50),
    ('Producto 6', 60),
    ('Producto 7', 70);

-- OFFSET sin LIMIT (salta primeras 3)
SELECT * FROM articulos OFFSET 3;

-- OFFSET con LIMIT (paginación)
SELECT * FROM articulos OFFSET 2 LIMIT 3;

-- Caso de uso: Página 2 con 3 items por página
-- Página 1: OFFSET 0 LIMIT 3
-- Página 2: OFFSET 3 LIMIT 3
-- Página 3: OFFSET 6 LIMIT 3

SELECT * FROM articulos
ORDER BY id
OFFSET 3 LIMIT 3;

/*
Output esperado:
 id | titulo | precio
----|--------|--------
  4 | Producto 4 | 40
  5 | Producto 5 | 50
  6 | Producto 6 | 60
*/
