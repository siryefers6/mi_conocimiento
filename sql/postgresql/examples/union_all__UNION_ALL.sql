/*
 * Objetivo: Combinar resultados de dos consultas incluyendo duplicados
 * Referencia: UNION ALL
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de compras 2023
CREATE TABLE IF NOT EXISTS compras_2023 (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Crear tabla de compras 2024
CREATE TABLE IF NOT EXISTS compras_2024 (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO compras_2023 (cliente, monto)
VALUES ('Juan', 500), ('María', 750);

INSERT INTO compras_2024 (cliente, monto)
VALUES ('Juan', 600), ('Carlos', 400);

-- UNION ALL (mantiene duplicados)
SELECT cliente, monto FROM compras_2023
UNION ALL
SELECT cliente, monto FROM compras_2024
ORDER BY cliente;

-- Contar registros con UNION ALL
SELECT COUNT(*) as total
FROM (
    SELECT cliente FROM compras_2023
    UNION ALL
    SELECT cliente FROM compras_2024
) as todas_compras;

/*
Output esperado:
 cliente | monto
---------|-------
 Carlos | 400
 Juan | 500
 Juan | 600
 María | 750
*/
