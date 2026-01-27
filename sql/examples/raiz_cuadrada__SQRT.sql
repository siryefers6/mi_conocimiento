/*
 * Objetivo: Calcular raíz cuadrada
 * Referencia: SQRT()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS areas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    area DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO areas (nombre, area)
VALUES
    ('Cuadrado A', 16),
    ('Cuadrado B', 25),
    ('Cuadrado C', 100),
    ('Cuadrado D', 144);

-- SQRT() calcula raíz cuadrada
SELECT nombre, area, SQRT(area) as lado FROM areas;

-- Verificar si es cuadrado perfecto
SELECT nombre, area, SQRT(area) as raiz, 
       ROUND(SQRT(area)) as raiz_aprox
FROM areas;

-- Usando SQRT en cálculos
SELECT 5 * SQRT(2) as diagonal_cuadrado_lado_5;

/*
Output esperado:
    nombre   | area | lado
---------------|------|------
 Cuadrado A | 16 | 4
 Cuadrado B | 25 | 5
 Cuadrado C | 100 | 10
 Cuadrado D | 144 | 12
*/
