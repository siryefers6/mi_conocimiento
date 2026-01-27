/*
 * Objetivo: Usar una subconsulta como tabla (tabla derivada)
 * Referencia: Subconsulta en FROM
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    vendedor VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO ventas (vendedor, monto)
VALUES
    ('Juan', 500),
    ('Juan', 700),
    ('María', 1500),
    ('María', 800),
    ('Carlos', 300),
    ('Carlos', 400);

-- Subconsulta en FROM
SELECT vendedor, total_ventas
FROM (
    SELECT vendedor, SUM(monto) as total_ventas
    FROM ventas
    GROUP BY vendedor
) as resumen_ventas
WHERE total_ventas > 1000
ORDER BY total_ventas DESC;

-- Subconsulta con múltiples columnas
SELECT vendedor, total_ventas, promedio_venta
FROM (
    SELECT
        vendedor,
        SUM(monto) as total_ventas,
        AVG(monto) as promedio_venta,
        COUNT(*) as cantidad
    FROM ventas
    GROUP BY vendedor
) as analisis
WHERE cantidad >= 2;

/*
Output esperado:
 vendedor | total_ventas
----------|---------------
 María | 2300
 Juan | 1200
*/
