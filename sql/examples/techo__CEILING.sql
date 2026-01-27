/*
 * Objetivo: Redondear hacia arriba (techo)
 * Referencia: CEILING()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS distancias (
    id SERIAL PRIMARY KEY,
    metros DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO distancias (metros)
VALUES
    (19.1),
    (49.5),
    (100.01),
    (5.99);

-- CEILING() redondea hacia arriba
SELECT metros, CEILING(metros) as techo FROM distancias;

-- Cálculo de palets necesarios
SELECT 
    metros,
    CEILING(metros / 10) as palets_necesarios
FROM distancias;

-- Redondear a múltiplo de 5
SELECT metros, CEILING(metros / 5) * 5 as redondeado_5 FROM distancias;

/*
Output esperado:
 metros | techo
--------|-------
 19.1 | 20
 49.5 | 50
 100.01 | 101
 5.99 | 6
*/
