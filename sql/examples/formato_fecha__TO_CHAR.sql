/*
 * Objetivo: Formatear una fecha en un formato específico
 * Referencia: TO_CHAR()
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS eventos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha TIMESTAMP
);

-- Insertar datos
INSERT INTO eventos (nombre, fecha)
VALUES
    ('Conferencia', '2024-03-15 14:30:00'),
    ('Reunión', '2024-05-20 09:00:00'),
    ('Presentación', '2024-07-10 16:45:00');

-- TO_CHAR() formatea la fecha
SELECT nombre, TO_CHAR(fecha, 'DD/MM/YYYY') as fecha_formateada FROM eventos;

-- Formato con hora
SELECT nombre, TO_CHAR(fecha, 'DD/MM/YYYY HH:MM:SS') as fecha_hora FROM eventos;

-- Formato con nombre de mes
SELECT nombre, TO_CHAR(fecha, 'DD de Month YYYY') as fecha_legible FROM eventos;

-- Formato personalizado
SELECT 
    nombre,
    TO_CHAR(fecha, 'Day, DD-Mon-YYYY') as formato_anglosajón,
    TO_CHAR(fecha, 'DD/MM/YYYY') as formato_español
FROM eventos;

/*
Output esperado:
     nombre    | fecha_formateada
-------------|------------------
 Conferencia | 15/03/2024
 Reunión | 20/05/2024
 Presentación | 10/07/2024
*/
