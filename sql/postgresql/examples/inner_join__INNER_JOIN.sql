/*
 * Objetivo: Combinar filas de dos tablas con coincidencias
 * Referencia: INNER JOIN
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de empleados
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento_id INT
);

-- Crear tabla de departamentos
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Insertar datos
INSERT INTO empleados (nombre, departamento_id)
VALUES ('Juan', 1), ('María', 1), ('Carlos', 2), ('Ana', 2), ('Luis', NULL);

INSERT INTO departamentos (nombre)
VALUES ('IT'), ('Ventas'), ('RR.HH.');

-- INNER JOIN (solo coincidencias)
SELECT e.nombre as empleado, d.nombre as departamento
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

-- INNER JOIN con múltiples columnas
SELECT e.id, e.nombre, d.id as dep_id, d.nombre as dep_nombre
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id
ORDER BY d.nombre;

/*
Output esperado:
 empleado | departamento
----------|---------------
 Juan | IT
 María | IT
 Carlos | Ventas
 Ana | Ventas
*/
