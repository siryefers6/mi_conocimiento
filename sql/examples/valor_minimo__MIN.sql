/*
 * Objetivo: Encontrar el valor mínimo de una columna
 * Referencia: MIN()
 * Tipo: función de agregación
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS precios (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100),
    tienda VARCHAR(50),
    precio DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO precios (producto, tienda, precio)
VALUES
    ('Laptop', 'Tienda A', 999.99),
    ('Laptop', 'Tienda B', 950.00),
    ('Laptop', 'Tienda C', 1020.50),
    ('Mouse', 'Tienda A', 29.99),
    ('Mouse', 'Tienda B', 24.99),
    ('Mouse', 'Tienda C', 32.99),
    ('Teclado', 'Tienda A', 79.99),
    ('Teclado', 'Tienda B', 69.99),
    ('Teclado', 'Tienda C', 85.50);

-- MIN básico
SELECT MIN(precio) as precio_minimo FROM precios;

-- MIN por producto
SELECT producto, MIN(precio) as precio_minimo
FROM precios
GROUP BY producto
ORDER BY precio_minimo;

-- MIN con WHERE
SELECT MIN(precio) as precio_minimo_laptops
FROM precios
WHERE producto = 'Laptop';

-- Encontrar tienda con precio más bajo
SELECT producto, tienda, precio
FROM precios
WHERE precio = (SELECT MIN(precio) FROM precios);

/*
Output esperado:
 precio_minimo
---------------
 24.99
*/
