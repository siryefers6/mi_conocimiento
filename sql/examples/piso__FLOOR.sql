/*
 * Objetivo: Redondear hacia abajo (piso)
 * Referencia: FLOOR()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS precios (
    id SERIAL PRIMARY KEY,
    precio DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO precios (precio)
VALUES
    (19.99),
    (49.50),
    (99.95),
    (5.45);

-- FLOOR() redondea hacia abajo
SELECT precio, FLOOR(precio) as piso FROM precios;

-- FLOOR combinado con cálculos
SELECT precio, FLOOR(precio * 100) / 100 as precio_piso FROM precios;

-- Dividir en grupos de 10
SELECT 
    precio,
    FLOOR(precio / 10) * 10 as rango_precio
FROM precios;

/*
Output esperado:
 precio | piso
--------|------
 19.99 | 19
 49.50 | 49
 99.95 | 99
 5.45 | 5
*/
