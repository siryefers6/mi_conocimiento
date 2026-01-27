/*
 * Objetivo: Insertar múltiples filas en una sola operación
 * Referencia: INSERT INTO VALUES (múltiple)
 * Tipo: DML (Data Manipulation Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Insertar múltiples filas en una operación
INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Laptop', 999.99, 5),
    ('Mouse', 29.99, 50),
    ('Teclado', 79.99, 30),
    ('Monitor', 299.99, 10),
    ('Cable USB', 9.99, 100);

-- Ver datos insertados
SELECT * FROM productos;

-- Contar filas insertadas
SELECT COUNT(*) as total FROM productos;

/*
Output esperado:
 id |  nombre  | precio | stock
----|----------|--------|-------
  1 | Laptop | 999.99 | 5
  2 | Mouse | 29.99 | 50
  3 | Teclado | 79.99 | 30
  4 | Monitor | 299.99 | 10
  5 | Cable USB | 9.99 | 100
*/
