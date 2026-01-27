/*
 * Objetivo: Seleccionar todas las columnas de una tabla
 * Referencia: SELECT *
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    ciudad VARCHAR(50),
    saldo DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO clientes (nombre, email, ciudad, saldo)
VALUES
    ('Juan García', 'juan@email.com', 'Madrid', 5000),
    ('María López', 'maria@email.com', 'Barcelona', 7500),
    ('Carlos Ruiz', 'carlos@email.com', 'Valencia', 3200);

-- SELECT * devuelve todas las columnas
SELECT * FROM clientes;

-- SELECT * con WHERE
SELECT * FROM clientes WHERE saldo > 4000;

/*
Output esperado:
 id |    nombre    |      email       |  ciudad   | saldo
----|--------------|------------------|-----------|--------
  1 | Juan García | juan@email.com | Madrid | 5000.00
  2 | María López | maria@email.com | Barcelona | 7500.00
  3 | Carlos Ruiz | carlos@email.com | Valencia | 3200.00
*/
