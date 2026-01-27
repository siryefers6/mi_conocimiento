/*
 * Objetivo: Encontrar filas de la primera consulta que no están en la segunda
 * Referencia: EXCEPT
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de usuarios registrados
CREATE TABLE IF NOT EXISTS usuarios_registrados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla de usuarios activos
CREATE TABLE IF NOT EXISTS usuarios_activos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Insertar datos
INSERT INTO usuarios_registrados (nombre)
VALUES ('Juan'), ('María'), ('Carlos'), ('Ana');

INSERT INTO usuarios_activos (nombre)
VALUES ('Juan'), ('María');

-- EXCEPT (registrados pero no activos)
SELECT nombre FROM usuarios_registrados
EXCEPT
SELECT nombre FROM usuarios_activos
ORDER BY nombre;

-- EXCEPT para encontrar diferencias
SELECT COUNT(*) as usuarios_inactivos
FROM (
    SELECT nombre FROM usuarios_registrados
    EXCEPT
    SELECT nombre FROM usuarios_activos
) as inactivos;

/*
Output esperado:
 nombre
--------
 Ana
 Carlos
*/
