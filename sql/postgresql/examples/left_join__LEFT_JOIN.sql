/*
 * Objetivo: Combinar tabla izquierda con coincidencias de tabla derecha
 * Referencia: LEFT JOIN
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
VALUES (1, 500), (1, 300), (2, 1000), (4, 250);

-- LEFT JOIN (todos de tabla izquierda + coincidencias)
SELECT c.nombre, COUNT(p.id) as total_pedidos, SUM(p.monto) as total_monto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre
ORDER BY total_monto DESC NULLS LAST;

-- LEFT JOIN con WHERE
SELECT c.nombre, p.monto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE p.id IS NULL;

/*
Output esperado:
 nombre | total_pedidos | total_monto
--------|---------------|-------------
 Juan | 2 | 800
 María | 1 | 1000
 Ana | 1 | 250
 Carlos | 0 |
*/
