/*
 * Objetivo: Elevar un número a una potencia
 * Referencia: POWER()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS exponentes (
    id SERIAL PRIMARY KEY,
    base INT,
    exponente INT
);

-- Insertar datos
INSERT INTO exponentes (base, exponente)
VALUES
    (2, 3),
    (3, 2),
    (5, 3),
    (10, 2);

-- POWER() eleva a potencia
SELECT base, exponente, POWER(base, exponente) as resultado FROM exponentes;

-- Cálculo de interés compuesto
SELECT 1000 * POWER(1.05, 10) as capital_final;

-- Tabla de potencias
SELECT 
    2 as base,
    n as exponente,
    POWER(2, n) as resultado
FROM (VALUES (1), (2), (3), (4), (5)) as t(n);

/*
Output esperado:
 base | exponente | resultado
------|-----------|----------
   2 | 3 | 8
   3 | 2 | 9
   5 | 3 | 125
  10 | 2 | 100
*/
