/*
 * Objetivo: Extraer una parte de una cadena
 * Referencia: SUBSTRING()
 * Tipo: función de texto
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS codigos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(50)
);

-- Insertar datos
INSERT INTO codigos (codigo)
VALUES
    ('ABC123DEF456'),
    ('XYZ789QWE012'),
    ('PQR345STU678');

-- SUBSTRING: extraer parte del texto
SELECT SUBSTRING(codigo, 1, 3) as prefijo FROM codigos;

-- SUBSTRING con rango
SELECT codigo, SUBSTRING(codigo, 4, 3) as numeros FROM codigos;

-- SUBSTRING desde posición
SELECT SUBSTRING(codigo FROM 7) as sufijo FROM codigos;

-- Extraer año de una fecha (formato texto)
SELECT SUBSTRING('2024-01-15', 1, 4) as anio;

/*
Output esperado:
 prefijo
---------
 ABC
 XYZ
 PQR
*/
