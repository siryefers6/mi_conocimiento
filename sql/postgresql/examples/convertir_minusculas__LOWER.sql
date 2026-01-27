/*
 * Objetivo: Convertir texto a minúsculas
 * Referencia: LOWER()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS marcas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Insertar datos
INSERT INTO marcas (nombre, email)
VALUES
    ('APPLE', 'CONTACTO@APPLE.COM'),
    ('Microsoft', 'info@microsoft.com'),
    ('GOOGLE', 'SUPPORT@GOOGLE.COM');

-- LOWER() convierte a minúsculas
SELECT LOWER(nombre) as nombre_minuscula FROM marcas;

-- LOWER en condición
SELECT * FROM marcas WHERE LOWER(nombre) = 'apple';

-- Normalizar emails
SELECT LOWER(email) as email_normalizado FROM marcas;

/*
Output esperado:
 nombre_minuscula
-----------------
 apple
 microsoft
 google
*/
