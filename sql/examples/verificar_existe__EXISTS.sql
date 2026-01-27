/*
 * Objetivo: Verificar la existencia de registros en una subconsulta
 * Referencia: EXISTS
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    monto DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO clientes (nombre)
VALUES ('Juan'), ('María'), ('Carlos'), ('Ana');

INSERT INTO pedidos (cliente_id, monto)
VALUES (1, 500), (1, 300), (2, 1000), (2, 250);

-- EXISTS: clientes que tienen al menos un pedido
SELECT nombre
FROM clientes c
WHERE EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id);

-- NOT EXISTS: clientes sin pedidos
SELECT nombre
FROM clientes c
WHERE NOT EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id);

-- EXISTS con SUM
SELECT nombre,
    (SELECT SUM(monto) FROM pedidos WHERE cliente_id = c.id) as total
FROM clientes c
WHERE EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.id);

/*
Output esperado (EXISTS):
 nombre
--------
 Juan
 María
*/
