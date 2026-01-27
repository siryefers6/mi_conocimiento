/*
 * Objetivo: Crear índice en múltiples columnas
 * Referencia: COMPOSITE INDEX
 * Tipo: optimización
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS pedidos_hist (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    fecha DATE,
    monto DECIMAL(10,2)
);

-- Insertar datos de ejemplo
INSERT INTO pedidos_hist (cliente_id, producto_id, fecha, monto)
VALUES
    (1, 10, '2024-01-15', 500),
    (1, 20, '2024-01-20', 750),
    (2, 10, '2024-02-05', 1000);

-- Crear índice compuesto
CREATE INDEX idx_pedidos_cliente_fecha ON pedidos_hist(cliente_id, fecha);

-- Crear otro índice compuesto
CREATE INDEX idx_pedidos_producto_cliente ON pedidos_hist(producto_id, cliente_id);

-- Ver índices
\di pedidos_hist

-- Consultas que usan el índice
SELECT * FROM pedidos_hist WHERE cliente_id = 1 AND fecha > '2024-01-01';

/*
Índices compuestos:
- Útiles para consultas con múltiples condiciones
- El orden importa: primero se busca por cliente, luego por fecha
- Pueden acelerar búsquedas en ambas columnas
*/
