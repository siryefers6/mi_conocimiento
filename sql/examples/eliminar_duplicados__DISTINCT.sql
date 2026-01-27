/*
 * Objetivo: Eliminar filas duplicadas del resultado
 * Referencia: DISTINCT
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ciudades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    pais VARCHAR(50)
);

-- Insertar datos con duplicados
INSERT INTO ciudades (nombre, pais)
VALUES
    ('Madrid', 'España'),
    ('Barcelona', 'España'),
    ('Madrid', 'España'),
    ('Londres', 'Reino Unido'),
    ('París', 'Francia'),
    ('Londres', 'Reino Unido');

-- Sin DISTINCT (muestra duplicados)
SELECT nombre FROM ciudades;

-- Con DISTINCT (sin duplicados)
SELECT DISTINCT nombre FROM ciudades;

-- DISTINCT con múltiples columnas
SELECT DISTINCT nombre, pais FROM ciudades;

/*
Output esperado (sin DISTINCT):
  nombre
----------
 Madrid
 Barcelona
 Madrid
 Londres
 París
 Londres

Output esperado (con DISTINCT):
  nombre
----------
 Madrid
 Barcelona
 Londres
 París
*/
