/*
 * Objetivo: Eliminar registros condicionalmente
 * Referencia: DELETE WHERE
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

-- Insertar datos de prueba
INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Laptop', 999.99, 0),
    ('Mouse', 29.99, 50),
    ('Teclado', 79.99, 0),
    ('Monitor', 299.99, 10);

-- Eliminar productos sin stock
DELETE FROM productos WHERE stock = 0;

-- Eliminar con condición AND
DELETE FROM productos WHERE stock = 0 AND precio < 100;

-- Eliminar con condición OR
DELETE FROM productos WHERE nombre = 'Mouse' OR precio > 500;

-- Ver registros restantes
SELECT * FROM productos;

/*
Output esperado:
 id |  nombre  | precio | stock
----|----------|--------|-------
 4 | Monitor | 299.99 | 10
*/
