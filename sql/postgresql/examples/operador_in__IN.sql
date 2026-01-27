/*
 * Objetivo: Verificar si un valor está en una lista
 * Referencia: IN
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    numero INT,
    estado VARCHAR(50),
    cliente_id INT
);

-- Insertar datos de prueba
INSERT INTO pedidos (numero, estado, cliente_id)
VALUES
    (1001, 'COMPLETADO', 101),
    (1002, 'PENDIENTE', 102),
    (1003, 'COMPLETADO', 103),
    (1004, 'CANCELADO', 104),
    (1005, 'PENDIENTE', 105);

-- IN simple
SELECT * FROM pedidos WHERE estado IN ('COMPLETADO', 'PENDIENTE');

-- IN con números
SELECT * FROM pedidos WHERE cliente_id IN (101, 103, 105);

-- IN con múltiples valores
SELECT numero, estado FROM pedidos
WHERE estado IN ('CANCELADO', 'DEVUELTO', 'RECHAZADO');

-- NOT IN
SELECT * FROM pedidos WHERE estado NOT IN ('CANCELADO');

/*
Output esperado:
 id | numero |   estado   | cliente_id
----|--------|------------|------------
  1 | 1001 | COMPLETADO | 101
  2 | 1002 | PENDIENTE | 102
  3 | 1003 | COMPLETADO | 103
  5 | 1005 | PENDIENTE | 105
*/
