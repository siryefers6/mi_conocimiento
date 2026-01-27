/*
 * Objetivo: Crear una vista materializada (cached)
 * Referencia: CREATE MATERIALIZED VIEW
 * Tipo: vista
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    vendedor VARCHAR(50),
    monto DECIMAL(10,2),
    fecha DATE
);

-- Insertar muchos datos (simulado)
INSERT INTO ventas (vendedor, monto, fecha)
VALUES
    ('Juan', 500, '2024-01-01'),
    ('Juan', 700, '2024-01-02'),
    ('María', 1500, '2024-01-01'),
    ('María', 800, '2024-01-03'),
    ('Carlos', 300, '2024-01-02');

-- Crear vista materializada
CREATE MATERIALIZED VIEW vista_mat_resumen_ventas AS
SELECT 
    vendedor,
    COUNT(*) as cantidad_ventas,
    SUM(monto) as total_monto,
    AVG(monto) as promedio_monto
FROM ventas
GROUP BY vendedor;

-- Usar vista materializada
SELECT * FROM vista_mat_resumen_ventas;

-- Refrescar vista (recalcular datos)
REFRESH MATERIALIZED VIEW vista_mat_resumen_ventas;

-- Ver vistas materializadas
\dm

/*
Diferencias:
- Vista normal: Ejecuta consulta cada vez (lenta si es compleja)
- Vista materializada: Cachea resultados (rápida, datos pueden estar antiguos)
*/
