/*
 * Objetivo: Obtener el resto (módulo) de una división
 * Referencia: MOD()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS numeros (
    id SERIAL PRIMARY KEY,
    dividendo INT,
    divisor INT
);

-- Insertar datos
INSERT INTO numeros (dividendo, divisor)
VALUES
    (17, 5),
    (20, 3),
    (100, 7),
    (25, 4);

-- MOD() devuelve el resto
SELECT dividendo, divisor, MOD(dividendo, divisor) as resto FROM numeros;

-- Encontrar números pares e impares
SELECT 
    n as numero,
    CASE WHEN MOD(n, 2) = 0 THEN 'Par' ELSE 'Impar' END as tipo
FROM (VALUES (1), (2), (3), (4), (5), (6)) as t(n);

-- Distribuir en grupos
SELECT 
    id,
    MOD(id, 3) as grupo
FROM (SELECT 1 as id UNION ALL SELECT 2 UNION ALL SELECT 3 
      UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6) as t;

/*
Output esperado:
 dividendo | divisor | resto
-----------|---------|-------
    17 | 5 | 2
    20 | 3 | 2
   100 | 7 | 2
    25 | 4 | 1
*/
