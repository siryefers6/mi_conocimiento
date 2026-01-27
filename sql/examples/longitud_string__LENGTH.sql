/*
 * Objetivo: Obtener la longitud de una cadena de texto
 * Referencia: LENGTH()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS tweets (
    id SERIAL PRIMARY KEY,
    contenido VARCHAR(280)
);

-- Insertar datos
INSERT INTO tweets (contenido)
VALUES
    ('Hola mundo'),
    ('PostgreSQL es una base de datos relacional muy poderosa'),
    ('SQL');

-- LENGTH() devuelve la longitud
SELECT contenido, LENGTH(contenido) as caracteres FROM tweets;

-- WHERE con LENGTH
SELECT * FROM tweets WHERE LENGTH(contenido) > 20;

-- Contar tweets por longitud
SELECT 
    CASE 
        WHEN LENGTH(contenido) <= 50 THEN 'Corto'
        WHEN LENGTH(contenido) <= 150 THEN 'Medio'
        ELSE 'Largo'
    END as categoria,
    COUNT(*) as cantidad
FROM tweets
GROUP BY categoria;

/*
Output esperado:
   contenido   | caracteres
------------------|----------
 Hola mundo | 10
 PostgreSQL es una base de datos relacional muy poderosa | 58
 SQL | 3
*/
