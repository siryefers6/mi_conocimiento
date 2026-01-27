/*
 * Objetivo: Retorna NULL si dos valores son iguales
 * Referencia: NULLIF()
 * Tipo: función condicional
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS cambios_inventario (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100),
    cantidad_anterior INT,
    cantidad_actual INT
);

-- Insertar datos
INSERT INTO cambios_inventario (producto, cantidad_anterior, cantidad_actual)
VALUES
    ('Laptop', 10, 8),
    ('Mouse', 50, 50),
    ('Teclado', 30, 35),
    ('Monitor', 5, 5);

-- NULLIF: retorna NULL si son iguales
SELECT 
    producto,
    cantidad_anterior,
    cantidad_actual,
    NULLIF(cantidad_anterior, cantidad_actual) as cambio_detectado
FROM cambios_inventario;

-- Usar NULLIF para evitar división por cero
SELECT 
    1 / NULLIF(0, 0) as division_segura;

-- NULLIF en CASE
SELECT 
    producto,
    cantidad_anterior,
    cantidad_actual,
    CASE 
        WHEN NULLIF(cantidad_anterior, cantidad_actual) IS NULL THEN 'Sin cambios'
        ELSE 'Cambios detectados'
    END as estado
FROM cambios_inventario;

/*
Output esperado:
    producto    | cantidad_anterior | cantidad_actual | cambio_detectado
------------------|---------|----------|------------------
 Laptop | 10 | 8 | 10
 Mouse | 50 | 50 | NULL
 Teclado | 30 | 35 | 30
 Monitor | 5 | 5 | NULL
*/
