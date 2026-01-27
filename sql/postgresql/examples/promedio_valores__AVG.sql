/*
 * Objetivo: Calcular el promedio de valores
 * Referencia: AVG()
 * Tipo: función de agregación
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS calificaciones (
    id SERIAL PRIMARY KEY,
    estudiante VARCHAR(100),
    materia VARCHAR(50),
    nota DECIMAL(5,2)
);

-- Insertar datos de prueba
INSERT INTO calificaciones (estudiante, materia, nota)
VALUES
    ('Juan', 'Matemática', 85),
    ('Juan', 'Inglés', 92),
    ('Juan', 'Historia', 78),
    ('María', 'Matemática', 95),
    ('María', 'Inglés', 88),
    ('María', 'Historia', 91),
    ('Carlos', 'Matemática', 72),
    ('Carlos', 'Inglés', 80),
    ('Carlos', 'Historia', 75);

-- AVG básico
SELECT AVG(nota) as promedio_general FROM calificaciones;

-- AVG con WHERE
SELECT AVG(nota) as promedio_matematica FROM calificaciones WHERE materia = 'Matemática';

-- AVG por estudiante
SELECT estudiante, AVG(nota) as promedio_estudiante
FROM calificaciones
GROUP BY estudiante
ORDER BY promedio_estudiante DESC;

-- AVG con multiple GROUP BY
SELECT estudiante, materia, COUNT(*) as exams, AVG(nota) as promedio
FROM calificaciones
GROUP BY estudiante, materia;

/*
Output esperado:
 promedio_general
-----------------
 84.33
*/
