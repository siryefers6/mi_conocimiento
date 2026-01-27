/*
 * Objetivo: Analizar el plan de ejecución de una consulta
 * Referencia: EXPLAIN
 * Tipo: optimización
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Insertar datos
INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Laptop', 999.99, 5),
    ('Mouse', 29.99, 50),
    ('Teclado', 79.99, 30);

-- EXPLAIN: mostrar plan de ejecución
EXPLAIN SELECT * FROM productos WHERE id = 1;

-- EXPLAIN ANALYZE: ejecutar y mostrar estadísticas reales
EXPLAIN ANALYZE SELECT * FROM productos WHERE id = 1;

-- EXPLAIN con consulta más compleja
EXPLAIN ANALYZE
SELECT p.nombre, SUM(p.precio * p.stock) as valor_total
FROM productos p
WHERE p.stock > 10
GROUP BY p.nombre;

-- Ver información de secuencias
EXPLAIN SELECT * FROM productos WHERE nombre LIKE 'M%';

/*
EXPLAIN muestra:
- Tipo de escaneo (Seq Scan, Index Scan)
- Costo estimado
- Filas estimadas vs reales (con ANALYZE)
- Planes de ejecución alternativos

Usar para optimizar consultas lentas.
*/
