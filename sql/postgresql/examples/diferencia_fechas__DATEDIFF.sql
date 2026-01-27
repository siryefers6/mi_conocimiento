/*
 * Objetivo: Calcular diferencia entre dos fechas
 * Referencia: DATEDIFF() o resta de fechas
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_inicio DATE,
    fecha_fin DATE
);

-- Insertar datos
INSERT INTO proyectos (nombre, fecha_inicio, fecha_fin)
VALUES
    ('Proyecto A', '2024-01-01', '2024-03-15'),
    ('Proyecto B', '2024-02-01', '2024-06-30'),
    ('Proyecto C', '2023-11-15', '2024-01-31');

-- Diferencia en días (resta de fechas)
SELECT 
    nombre,
    fecha_inicio,
    fecha_fin,
    fecha_fin - fecha_inicio as dias_duracion
FROM proyectos;

-- Usando EXTRACT para semanas
SELECT 
    nombre,
    EXTRACT(EPOCH FROM (fecha_fin - fecha_inicio)) / 86400 as dias
FROM proyectos;

-- Proyectos activos
SELECT * FROM proyectos WHERE fecha_fin >= CURRENT_DATE;

/*
Output esperado:
    nombre    | fecha_inicio | fecha_fin | dias_duracion
-------------|-----|-----------|-------
 Proyecto A | 2024-01-01 | 2024-03-15 | 74
 Proyecto B | 2024-02-01 | 2024-06-30 | 150
 Proyecto C | 2023-11-15 | 2024-01-31 | 78
*/
