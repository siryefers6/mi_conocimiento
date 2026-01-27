/*
 * Objetivo: Filtrar filas basado en una condición
 * Referencia: WHERE
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO ventas (producto, cantidad, precio_unitario)
VALUES
    ('Laptop', 2, 999.99),
    ('Mouse', 10, 29.99),
    ('Teclado', 5, 79.99),
    ('Monitor', 1, 299.99),
    ('Cable', 15, 9.99);

-- WHERE simple (igualdad)
SELECT * FROM ventas WHERE cantidad = 10;

-- WHERE con comparación
SELECT * FROM ventas WHERE precio_unitario > 50;

-- WHERE con mayor que
SELECT * FROM ventas WHERE cantidad >= 5;

-- WHERE con menor que
SELECT * FROM ventas WHERE precio_unitario < 30;

/*
Output esperado:
 id | producto | cantidad | precio_unitario
----|----------|----------|----------------
  2 | Mouse | 10 | 29.99
*/
