/*
 * Objetivo: Encontrar filas comunes en dos consultas
 * Referencia: INTERSECT
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de empleados A
CREATE TABLE IF NOT EXISTS empleados_sucursal_a (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla de empleados B
CREATE TABLE IF NOT EXISTS empleados_sucursal_b (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Insertar datos
INSERT INTO empleados_sucursal_a (nombre)
VALUES ('Juan'), ('María'), ('Carlos');

INSERT INTO empleados_sucursal_b (nombre)
VALUES ('María'), ('Carlos'), ('Ana');

-- INTERSECT (solo registros comunes)
SELECT nombre FROM empleados_sucursal_a
INTERSECT
SELECT nombre FROM empleados_sucursal_b;

-- INTERSECT con COUNT
SELECT COUNT(*) as empleados_en_ambas_sucursales
FROM (
    SELECT nombre FROM empleados_sucursal_a
    INTERSECT
    SELECT nombre FROM empleados_sucursal_b
) as comun;

/*
Output esperado:
 nombre
--------
 Carlos
 María
*/
