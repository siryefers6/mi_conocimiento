/*
 * Objetivo: Usar CTE (Common Table Expression) con WITH
 * Referencia: WITH (CTE)
 * Tipo: vista
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    manager_id INT,
    salario DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO empleados (nombre, manager_id, salario)
VALUES
    ('CEO', NULL, 10000),
    ('Gerente IT', 1, 7000),
    ('Developer 1', 2, 4000),
    ('Developer 2', 2, 4500),
    ('Gerente Ventas', 1, 6000),
    ('Vendedor', 5, 3000);

-- CTE simple
WITH empleados_bien_pagados AS (
    SELECT nombre, salario FROM empleados WHERE salario > 4000
)
SELECT * FROM empleados_bien_pagados;

-- CTE múltiple
WITH directivos AS (
    SELECT * FROM empleados WHERE manager_id IS NULL OR salario > 5000
),
junior AS (
    SELECT * FROM empleados WHERE salario < 4500
)
SELECT 'Directivos' as categoria, COUNT(*) as cantidad FROM directivos
UNION ALL
SELECT 'Junior' as categoria, COUNT(*) as cantidad FROM junior;

-- CTE recursivo (jerarquía)
WITH RECURSIVE jerarquia AS (
    SELECT id, nombre, manager_id, 1 as nivel FROM empleados WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.nombre, e.manager_id, j.nivel + 1
    FROM empleados e
    JOIN jerarquia j ON e.manager_id = j.id
)
SELECT * FROM jerarquia;

/*
CTE (WITH):
- Define consulta temporal
- Más legible que subconsultas anidadas
- RECURSIVE para jerarquías
*/
