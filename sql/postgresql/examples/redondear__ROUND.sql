/*
 * Objetivo: Redondear un número a N decimales
 * Referencia: ROUND()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS mediciones (
    id SERIAL PRIMARY KEY,
    valor DECIMAL(10,4)
);

-- Insertar datos
INSERT INTO mediciones (valor)
VALUES
    (3.14159),
    (2.71828),
    (1.41421),
    (10.5555);

-- ROUND() redondea a N decimales
SELECT valor, ROUND(valor, 2) as redondeado_2 FROM mediciones;

-- ROUND() sin decimales
SELECT valor, ROUND(valor, 0) as entero FROM mediciones;

-- ROUND() con 3 decimales
SELECT ROUND(valor, 3) as redondeado_3 FROM mediciones;

-- Promedio redondeado
SELECT ROUND(AVG(valor), 2) as promedio FROM mediciones;

/*
Output esperado:
  valor  | redondeado_2
----------|---------------
 3.14159 | 3.14
 2.71828 | 2.72
 1.41421 | 1.41
 10.5555 | 10.56
*/
