/*
 * Objetivo: Filtrar grupos basado en una condición (HAVING)
 * Referencia: HAVING
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO pedidos (cliente, monto)
VALUES
    ('Juan', 500),
    ('Juan', 700),
    ('María', 1500),
    ('María', 2000),
    ('Carlos', 300),
    ('Carlos', 400),
    ('Carlos', 250);

-- GROUP BY con WHERE (filtra antes de agrupar)
SELECT cliente, COUNT(*) as cantidad FROM pedidos
WHERE monto > 400
GROUP BY cliente;

-- HAVING (filtra después de agrupar)
SELECT cliente, SUM(monto) as total, COUNT(*) as pedidos
FROM pedidos
GROUP BY cliente
HAVING SUM(monto) > 1000;

-- HAVING con múltiples condiciones
SELECT cliente, COUNT(*) as total_pedidos, AVG(monto) as promedio
FROM pedidos
GROUP BY cliente
HAVING COUNT(*) >= 2 AND AVG(monto) > 400;

/*
Output esperado (HAVING):
 cliente | total | pedidos
---------|-------|--------
 Juan | 1200 | 2
 María | 3500 | 2
*/
