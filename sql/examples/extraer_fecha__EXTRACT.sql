/*
 * Objetivo: Extraer parte de una fecha (día, mes, año, etc)
 * Referencia: EXTRACT()
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    monto DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO ventas (fecha, monto)
VALUES
    ('2024-01-15', 500),
    ('2024-02-20', 750),
    ('2024-03-10', 1000),
    ('2023-12-25', 600);

-- EXTRACT día
SELECT fecha, EXTRACT(DAY FROM fecha) as dia FROM ventas;

-- EXTRACT mes
SELECT fecha, EXTRACT(MONTH FROM fecha) as mes FROM ventas;

-- EXTRACT año
SELECT fecha, EXTRACT(YEAR FROM fecha) as anio FROM ventas;

-- Agrupar por mes
SELECT 
    EXTRACT(MONTH FROM fecha) as mes,
    SUM(monto) as total
FROM ventas
GROUP BY EXTRACT(MONTH FROM fecha)
ORDER BY mes;

/*
Output esperado:
   fecha   | dia
------------|-----
 2024-01-15 | 15
 2024-02-20 | 20
 2024-03-10 | 10
 2023-12-25 | 25
*/
