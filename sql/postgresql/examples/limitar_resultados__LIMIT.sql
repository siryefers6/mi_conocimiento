/*
 * Objetivo: Limitar la cantidad de filas en resultado
 * Referencia: LIMIT
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

-- Insertar muchos datos de prueba
INSERT INTO productos (nombre, precio)
VALUES
    ('Laptop', 999.99),
    ('Mouse', 29.99),
    ('Teclado', 79.99),
    ('Monitor', 299.99),
    ('Cable', 9.99),
    ('Hub USB', 49.99),
    ('SSD', 129.99),
    ('RAM', 99.99);

-- LIMIT devuelve solo primeras 3 filas
SELECT * FROM productos LIMIT 3;

-- LIMIT con número específico
SELECT nombre, precio FROM productos LIMIT 5;

-- LIMIT con ORDER BY (10 productos más caros)
SELECT nombre, precio FROM productos
ORDER BY precio DESC
LIMIT 3;

/*
Output esperado:
 id |  nombre  | precio
----|----------|--------
  1 | Laptop | 999.99
  2 | Mouse | 29.99
  3 | Teclado | 79.99
*/
