/*
 * Objetivo: Reemplazar texto dentro de una cadena
 * Referencia: REPLACE()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS plantillas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200)
);

-- Insertar datos
INSERT INTO plantillas (titulo)
VALUES
    ('Bienvenido a PostgreSQL'),
    ('PostgreSQL es increíble'),
    ('Aprende PostgreSQL hoy');

-- REPLACE() reemplaza texto
SELECT REPLACE(titulo, 'PostgreSQL', 'SQL') as titulo_modificado FROM plantillas;

-- Múltiples reemplazos (anidados)
SELECT 
    REPLACE(
        REPLACE(titulo, 'PostgreSQL', 'PSQL'),
        'a',
        '4'
    ) as titulo_modificado
FROM plantillas;

-- REPLACE con números
SELECT REPLACE('2024-01-15', '-', '/') as fecha_formateada;

/*
Output esperado:
   titulo_modificado
-----------------------
 Bienvenido a SQL
 SQL es increíble
 Aprende SQL hoy
*/
