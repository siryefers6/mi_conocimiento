/*
 * Objetivo: Encontrar el valor máximo de una columna
 * Referencia: MAX()
 * Tipo: función de agregación
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS temperaturas (
    id SERIAL PRIMARY KEY,
    ciudad VARCHAR(50),
    fecha DATE,
    temperatura INT
);

-- Insertar datos de prueba
INSERT INTO temperaturas (ciudad, fecha, temperatura)
VALUES
    ('Madrid', '2024-01-15', 28),
    ('Madrid', '2024-01-16', 32),
    ('Madrid', '2024-01-17', 30),
    ('Barcelona', '2024-01-15', 25),
    ('Barcelona', '2024-01-16', 28),
    ('Barcelona', '2024-01-17', 26),
    ('Valencia', '2024-01-15', 35),
    ('Valencia', '2024-01-16', 37),
    ('Valencia', '2024-01-17', 36);

-- MAX básico
SELECT MAX(temperatura) as temp_maxima FROM temperaturas;

-- MAX por ciudad
SELECT ciudad, MAX(temperatura) as temp_maxima
FROM temperaturas
GROUP BY ciudad
ORDER BY temp_maxima DESC;

-- MAX con WHERE
SELECT MAX(temperatura) as temp_maxima_madrid
FROM temperaturas
WHERE ciudad = 'Madrid';

-- MAX de múltiples columnas (en forma de subquery)
SELECT * FROM temperaturas WHERE temperatura = (SELECT MAX(temperatura) FROM temperaturas);

/*
Output esperado:
 temp_maxima
-------------
 37
*/
