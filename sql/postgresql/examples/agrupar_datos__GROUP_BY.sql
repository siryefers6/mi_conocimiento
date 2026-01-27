/*
 * Objetivo: Agrupar filas y calcular agregaciones
 * Referencia: GROUP BY
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    vendedor VARCHAR(100),
    monto DECIMAL(10,2),
    fecha DATE
);

-- Insertar datos de prueba
INSERT INTO ventas (vendedor, monto, fecha)
VALUES
    ('Juan', 1000, '2024-01-01'),
    ('María', 1500, '2024-01-01'),
    ('Juan', 800, '2024-01-02'),
    ('Carlos', 1200, '2024-01-02'),
    ('María', 900, '2024-01-03'),
    ('Juan', 1100, '2024-01-03');

-- GROUP BY simple
SELECT vendedor, COUNT(*) as total_ventas FROM ventas GROUP BY vendedor;

-- GROUP BY con SUM
SELECT vendedor, SUM(monto) as total_monto FROM ventas GROUP BY vendedor;

-- GROUP BY con múltiples columnas
SELECT vendedor, fecha, SUM(monto) as total_diario
FROM ventas
GROUP BY vendedor, fecha
ORDER BY vendedor, fecha;

/*
Output esperado:
 vendedor | total_ventas
----------|---------------
 Juan | 3
 María | 2
 Carlos | 1
*/
