/*
 * Objetivo: Condicional simple con CASE WHEN
 * Referencia: CASE WHEN ... THEN ... END
 * Tipo: función condicional
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    calificacion INT
);

-- Insertar datos
INSERT INTO estudiantes (nombre, calificacion)
VALUES
    ('Juan', 85),
    ('María', 92),
    ('Carlos', 78),
    ('Ana', 95),
    ('Luis', 68);

-- CASE WHEN simple
SELECT 
    nombre,
    calificacion,
    CASE 
        WHEN calificacion >= 90 THEN 'Excelente'
        WHEN calificacion >= 80 THEN 'Bueno'
        WHEN calificacion >= 70 THEN 'Regular'
        ELSE 'Insuficiente'
    END as desempenio
FROM estudiantes;

-- CASE con valores numéricos
SELECT 
    nombre,
    CASE 
        WHEN calificacion >= 90 THEN 5
        WHEN calificacion >= 80 THEN 4
        WHEN calificacion >= 70 THEN 3
        ELSE 2
    END as puntuacion
FROM estudiantes;

/*
Output esperado:
 nombre | calificacion | desempenio
--------|--------------|------------------
 Juan | 85 | Bueno
 María | 92 | Excelente
 Carlos | 78 | Regular
 Ana | 95 | Excelente
 Luis | 68 | Insuficiente
*/
