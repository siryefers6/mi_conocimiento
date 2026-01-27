/*
 * Objetivo: Combinar todas las filas de ambas tablas
 * Referencia: FULL OUTER JOIN
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla A
CREATE TABLE IF NOT EXISTS usuarios_sistema_antiguo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla B
CREATE TABLE IF NOT EXISTS usuarios_sistema_nuevo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Insertar datos
INSERT INTO usuarios_sistema_antiguo (nombre)
VALUES ('Juan'), ('María'), ('Carlos');

INSERT INTO usuarios_sistema_nuevo (nombre)
VALUES ('María'), ('Carlos'), ('Ana'), ('Luis');

-- FULL OUTER JOIN (todas las filas de ambas tablas)
SELECT
    COALESCE(a.nombre, b.nombre) as nombre,
    CASE WHEN a.id IS NOT NULL THEN 'Antiguo' ELSE 'Nuevo' END as origen
FROM usuarios_sistema_antiguo a
FULL OUTER JOIN usuarios_sistema_nuevo b ON a.nombre = b.nombre
ORDER BY nombre;

-- FULL OUTER JOIN para encontrar diferencias
SELECT
    a.nombre as antiguo,
    b.nombre as nuevo
FROM usuarios_sistema_antiguo a
FULL OUTER JOIN usuarios_sistema_nuevo b ON a.nombre = b.nombre
WHERE a.id IS NULL OR b.id IS NULL;

/*
Output esperado:
 nombre | origen
--------|--------
 Ana | Nuevo
 Carlos | Antiguo
 Juan | Antiguo
 Luis | Nuevo
 María | Antiguo
*/
