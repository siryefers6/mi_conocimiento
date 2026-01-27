/*
 * Objetivo: Ordenar resultados en forma descendente
 * Referencia: ORDER BY DESC
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS peliculas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150),
    director VARCHAR(100),
    anio INT,
    calificacion DECIMAL(3,1)
);

-- Insertar datos de prueba
INSERT INTO peliculas (titulo, director, anio, calificacion)
VALUES
    ('Avatar', 'James Cameron', 2009, 7.8),
    ('Titanic', 'James Cameron', 1997, 7.9),
    ('The Dark Knight', 'Christopher Nolan', 2008, 9.0),
    ('Inception', 'Christopher Nolan', 2010, 8.8),
    ('Pulp Fiction', 'Quentin Tarantino', 1994, 8.9);

-- ORDER BY DESC (descendente)
SELECT titulo, anio FROM peliculas ORDER BY anio DESC;

-- Películas ordenadas por calificación (mejores primero)
SELECT titulo, calificacion FROM peliculas ORDER BY calificacion DESC;

-- Múltiples columnas con diferentes direcciones
SELECT titulo, director, anio FROM peliculas
ORDER BY director ASC, anio DESC;

/*
Output esperado:
    titulo    | anio
--------------|------
 Inception | 2010
 Avatar | 2009
 The Dark Knight | 2008
 Titanic | 1997
 Pulp Fiction | 1994
*/
