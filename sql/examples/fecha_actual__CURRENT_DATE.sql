/*
 * Objetivo: Obtener la fecha actual
 * Referencia: CURRENT_DATE
 * Tipo: función de fecha
 * Nivel: básico
 */

-- Obtener fecha actual
SELECT CURRENT_DATE as hoy;

-- Crear tabla con fecha actual
CREATE TABLE IF NOT EXISTS registros (
    id SERIAL PRIMARY KEY,
    contenido VARCHAR(100),
    fecha DATE DEFAULT CURRENT_DATE
);

-- Insertar con fecha actual automática
INSERT INTO registros (contenido) VALUES ('Primer registro');

-- Comparar fechas
SELECT * FROM registros WHERE fecha = CURRENT_DATE;

-- Diferencia de días
SELECT 
    CURRENT_DATE as hoy,
    DATE '2024-01-01' as año_nuevo,
    CURRENT_DATE - DATE '2024-01-01' as dias_desde_ano_nuevo;

/*
Output esperado:
    hoy
----------
 2024-01-27
*/
