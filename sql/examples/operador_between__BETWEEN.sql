/*
 * Objetivo: Filtrar valores dentro de un rango
 * Referencia: BETWEEN
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Insertar datos de prueba
INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Laptop', 999.99, 5),
    ('Mouse', 29.99, 50),
    ('Teclado', 79.99, 30),
    ('Monitor', 299.99, 10),
    ('Cable', 9.99, 100),
    ('Hub USB', 49.99, 25);

-- BETWEEN incluye ambos valores
SELECT * FROM productos WHERE precio BETWEEN 50 AND 300;

-- BETWEEN con números enteros
SELECT nombre, stock FROM productos WHERE stock BETWEEN 10 AND 50;

-- NOT BETWEEN
SELECT * FROM productos WHERE precio NOT BETWEEN 50 AND 100;

-- BETWEEN con fechas (ejemplo)
-- SELECT * FROM ventas WHERE fecha BETWEEN '2024-01-01' AND '2024-12-31';

/*
Output esperado:
 id |  nombre  | precio | stock
----|----------|--------|-------
  3 | Teclado | 79.99 | 30
  4 | Monitor | 299.99 | 10
  6 | Hub USB | 49.99 | 25
*/
