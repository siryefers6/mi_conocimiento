/*
 * Objetivo: Convertir texto a mayúsculas
 * Referencia: UPPER()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS comentarios (
    id SERIAL PRIMARY KEY,
    texto VARCHAR(200)
);

-- Insertar datos
INSERT INTO comentarios (texto)
VALUES
    ('PostgreSQL es excelente'),
    ('Me encanta las bases de datos'),
    ('SQL es fundamental');

-- UPPER() convierte a mayúsculas
SELECT UPPER(texto) as texto_mayuscula FROM comentarios;

-- UPPER en WHERE
SELECT * FROM comentarios WHERE UPPER(texto) LIKE '%EXCELENTE%';

-- Combinado con CONCAT
SELECT id, UPPER(texto) || '!!!' as mensaje FROM comentarios;

/*
Output esperado:
     texto_mayuscula
-------------------------------------
 POSTGRESQL ES EXCELENTE
 ME ENCANTA LAS BASES DE DATOS
 SQL ES FUNDAMENTAL
*/
