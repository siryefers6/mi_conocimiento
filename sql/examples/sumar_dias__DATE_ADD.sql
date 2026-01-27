/*
 * Objetivo: Sumar días a una fecha
 * Referencia: DATE_ADD() o +
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS tareas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    fecha_creacion DATE,
    plazo INT -- días de plazo
);

-- Insertar datos
INSERT INTO tareas (titulo, fecha_creacion, plazo)
VALUES
    ('Tarea 1', '2024-01-15', 7),
    ('Tarea 2', '2024-01-20', 14),
    ('Tarea 3', '2024-01-10', 5);

-- Sumar días a fecha (resta)
SELECT 
    titulo,
    fecha_creacion,
    plazo,
    fecha_creacion + plazo as fecha_vencimiento
FROM tareas;

-- Usando INTERVAL
SELECT 
    CURRENT_DATE as hoy,
    CURRENT_DATE + INTERVAL '7 days' as en_una_semana,
    CURRENT_DATE + INTERVAL '1 month' as en_un_mes;

-- Fechas de vencimiento cercanas
SELECT titulo, fecha_creacion + plazo as vencimiento
FROM tareas
WHERE (fecha_creacion + plazo) <= CURRENT_DATE + 3;

/*
Output esperado:
    titulo     | fecha_creacion | plazo | fecha_vencimiento
----------------|--------|-------|----------
 Tarea 1 | 2024-01-15 | 7 | 2024-01-22
 Tarea 2 | 2024-01-20 | 14 | 2024-02-03
 Tarea 3 | 2024-01-10 | 5 | 2024-01-15
*/
