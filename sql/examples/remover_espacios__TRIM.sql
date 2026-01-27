/*
 * Objetivo: Remover espacios en blanco de los extremos
 * Referencia: TRIM()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS textos_sucios (
    id SERIAL PRIMARY KEY,
    contenido VARCHAR(100)
);

-- Insertar datos con espacios extras
INSERT INTO textos_sucios (contenido)
VALUES
    ('  PostgreSQL  '),
    ('   Bases de Datos   '),
    ('SQL'),
    ('  Trimmed  ');

-- TRIM() remueve espacios de ambos lados
SELECT contenido, TRIM(contenido) as limpio FROM textos_sucios;

-- LTRIM() remueve del lado izquierdo
SELECT LTRIM(contenido) as sin_espacios_izq FROM textos_sucios;

-- RTRIM() remueve del lado derecho
SELECT RTRIM(contenido) as sin_espacios_der FROM textos_sucios;

-- Usar TRIM en WHERE
SELECT * FROM textos_sucios WHERE TRIM(contenido) = 'PostgreSQL';

/*
Output esperado:
  contenido   | limpio
-----------------|-------------
   PostgreSQL   | PostgreSQL
   Bases de Datos    | Bases de Datos
 SQL | SQL
   Trimmed   | Trimmed
*/
