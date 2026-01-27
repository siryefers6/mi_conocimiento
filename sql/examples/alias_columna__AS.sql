/*
 * Objetivo: Renombrar columnas en el resultado con alias
 * Referencia: AS
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    numero_pedido INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    fecha TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO pedidos (numero_pedido, cantidad, precio_unitario, fecha)
VALUES
    (101, 5, 99.99, CURRENT_TIMESTAMP),
    (102, 3, 49.99, CURRENT_TIMESTAMP),
    (103, 10, 29.99, CURRENT_TIMESTAMP);

-- Usar AS para renombrar columnas
SELECT
    numero_pedido AS "Pedido #",
    cantidad AS "Cantidad Productos",
    precio_unitario AS "Precio Unit.",
    (cantidad * precio_unitario) AS "Total"
FROM pedidos;

-- Sin comillas el alias se convierte a minúsculas
SELECT
    numero_pedido as numero,
    cantidad as qty
FROM pedidos;

/*
Output esperado:
 Pedido # | Cantidad Productos | Precio Unit. | Total
----------|-------------------|--------------|--------
 101 | 5 | 99.99 | 499.95
 102 | 3 | 49.99 | 149.97
 103 | 10 | 29.99 | 299.90
*/
