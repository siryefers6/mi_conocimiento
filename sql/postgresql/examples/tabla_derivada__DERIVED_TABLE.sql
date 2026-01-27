/*
 * Objetivo: Usar tabla derivada (subconsulta en FROM)
 * Referencia: Tabla derivada (derived table)
 * Tipo: vista
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ordenes (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(50),
    monto DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO ordenes (cliente, monto)
VALUES
    ('Juan', 500),
    ('Juan', 700),
    ('María', 1500),
    ('María', 800),
    ('Carlos', 300),
    ('Carlos', 400);

-- Usar tabla derivada
SELECT cliente, promedio_orden
FROM (
    SELECT 
        cliente,
        AVG(monto) as promedio_orden
    FROM ordenes
    GROUP BY cliente
) as resumen
WHERE promedio_orden > 400;

-- Tabla derivada con LIMIT
SELECT top_clientes.cliente, top_clientes.total
FROM (
    SELECT cliente, SUM(monto) as total
    FROM ordenes
    GROUP BY cliente
    ORDER BY total DESC
    LIMIT 3
) as top_clientes;

-- Tabla derivada anidada
SELECT *
FROM (
    SELECT cliente, COUNT(*) as cantidad
    FROM (
        SELECT * FROM ordenes WHERE monto > 500
    ) as ordenes_grandes
    GROUP BY cliente
) as resumen;

/*
Tabla derivada:
- Subconsulta temporal en FROM
- Se ejecuta cada vez (a diferencia de vista materializada)
- Útil para consultas únicas y complejas
*/
