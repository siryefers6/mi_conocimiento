/*
 * Objetivo: Contar cantidad de filas
 * Referencia: COUNT()
 * Tipo: función de agregación
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    grado VARCHAR(20),
    edad INT
);

-- Insertar datos de prueba
INSERT INTO estudiantes (nombre, grado, edad)
VALUES
    ('Juan', '10A', 16),
    ('María', '10A', 16),
    ('Carlos', '10B', 17),
    ('Ana', '10B', 16),
    ('Luis', '10C', 17);

-- COUNT(*) cuenta todas las filas
SELECT COUNT(*) as total_estudiantes FROM estudiantes;

-- COUNT con columna (cuenta no-nulos)
SELECT COUNT(edad) FROM estudiantes;

-- COUNT(DISTINCT) cuenta valores únicos
SELECT COUNT(DISTINCT grado) as total_grados FROM estudiantes;

-- COUNT con GROUP BY
SELECT grado, COUNT(*) as estudiantes_por_grado
FROM estudiantes
GROUP BY grado;

/*
Output esperado:
 total_estudiantes
------------------
 5
*/
