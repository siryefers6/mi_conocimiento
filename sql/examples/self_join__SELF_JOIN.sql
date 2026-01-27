/*
 * Objetivo: Unir tabla consigo misma
 * Referencia: SELF JOIN
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de empleados (con manager)
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    manager_id INT
);

-- Insertar datos (algunos empleados tienen manager)
INSERT INTO empleados (nombre, manager_id)
VALUES
    ('Juan (CEO)', NULL),
    ('María (Gerente IT)', 1),
    ('Carlos (Dev)', 2),
    ('Ana (Dev)', 2),
    ('Luis (Gerente Ventas)', 1),
    ('Paula (Vendedor)', 5);

-- SELF JOIN para ver empleados y sus managers
SELECT
    e.nombre as empleado,
    m.nombre as manager
FROM empleados e
LEFT JOIN empleados m ON e.manager_id = m.id;

-- SELF JOIN para encontrar empleados sin manager
SELECT e.nombre
FROM empleados e
LEFT JOIN empleados m ON e.manager_id = m.id
WHERE m.id IS NULL;

-- Contar empleados por manager
SELECT m.nombre as manager, COUNT(e.id) as cantidad_empleados
FROM empleados e
JOIN empleados m ON e.manager_id = m.id
GROUP BY m.id, m.nombre;

/*
Output esperado:
 empleado | manager
-----------|------------------
 Juan (CEO) | NULL
 María (Gerente IT) | Juan (CEO)
 Carlos (Dev) | María (Gerente IT)
 Ana (Dev) | María (Gerente IT)
 Luis (Gerente Ventas) | Juan (CEO)
 Paula (Vendedor) | Luis (Gerente Ventas)
*/
