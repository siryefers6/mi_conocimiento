/*
 * Objetivo: Combinar múltiples condiciones con OR (al menos una debe cumplirse)
 * Referencia: OR
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    saldo DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO clientes (nombre, ciudad, saldo)
VALUES
    ('Juan', 'Madrid', 5000),
    ('María', 'Barcelona', 7500),
    ('Carlos', 'Valencia', 3200),
    ('Ana', 'Madrid', 1500);

-- OR: al menos una condición debe ser verdadera
SELECT * FROM clientes WHERE ciudad = 'Madrid' OR ciudad = 'Barcelona';

-- OR con condiciones diferentes
SELECT * FROM clientes
WHERE saldo > 6000 OR nombre = 'Carlos';

-- Múltiples OR
SELECT nombre, ciudad FROM clientes
WHERE ciudad = 'Madrid' OR ciudad = 'Barcelona' OR ciudad = 'Valencia';

/*
Output esperado:
 id |  nombre | ciudad | saldo
----|---------|--------|--------
  1 | Juan | Madrid | 5000
  2 | María | Barcelona | 7500
  3 | Carlos | Valencia | 3200
*/
