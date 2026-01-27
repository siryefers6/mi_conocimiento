/*
 * Objetivo: Concatenar múltiples cadenas de texto
 * Referencia: CONCAT() o ||
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    ciudad VARCHAR(50)
);

-- Insertar datos
INSERT INTO personas (nombre, apellido, ciudad)
VALUES
    ('Juan', 'García', 'Madrid'),
    ('María', 'López', 'Barcelona'),
    ('Carlos', 'Rodríguez', 'Valencia');

-- Concatenar con ||
SELECT nombre || ' ' || apellido as nombre_completo FROM personas;

-- Concatenar con CONCAT()
SELECT CONCAT(nombre, ' ', apellido, ' de ', ciudad) as descripcion FROM personas;

-- Concatenar en WHERE
SELECT * FROM personas
WHERE nombre || ' ' || apellido = 'Juan García';

/*
Output esperado:
 nombre_completo
-----------------
 Juan García
 María López
 Carlos Rodríguez
*/
