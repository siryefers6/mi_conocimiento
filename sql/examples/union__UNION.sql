/*
 * Objetivo: Combinar resultados de dos consultas sin duplicados
 * Referencia: UNION
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de clientes antiguos
CREATE TABLE IF NOT EXISTS clientes_antiguos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Crear tabla de clientes nuevos
CREATE TABLE IF NOT EXISTS clientes_nuevos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Insertar datos
INSERT INTO clientes_antiguos (nombre, email)
VALUES ('Juan', 'juan@email.com'), ('María', 'maria@email.com');

INSERT INTO clientes_nuevos (nombre, email)
VALUES ('María', 'maria@email.com'), ('Carlos', 'carlos@email.com');

-- UNION (sin duplicados)
SELECT nombre, email FROM clientes_antiguos
UNION
SELECT nombre, email FROM clientes_nuevos
ORDER BY nombre;

-- UNION con DISTINCT explícito
SELECT nombre FROM clientes_antiguos
UNION
SELECT nombre FROM clientes_nuevos;

/*
Output esperado:
 nombre |       email
--------|-------------------
 Carlos | carlos@email.com
 Juan | juan@email.com
 María | maria@email.com
*/
