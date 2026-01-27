/*
 * Objetivo: Deshacer (revertir) una transacción
 * Referencia: ROLLBACK
 * Tipo: control de transacciones
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS transacciones (
    id SERIAL PRIMARY KEY,
    operacion VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Insertar datos iniciales
INSERT INTO transacciones (operacion, monto)
VALUES
    ('Operación A', 1000),
    ('Operación B', 500);

-- Iniciar transacción
BEGIN;

-- Realizar operaciones
INSERT INTO transacciones (operacion, monto) VALUES ('Operación C', 750);
DELETE FROM transacciones WHERE id = 2;

-- Ver cambios (dentro de la transacción)
SELECT * FROM transacciones;

-- ROLLBACK: deshacer todos los cambios
ROLLBACK;

-- Los cambios fueron revertidos
SELECT * FROM transacciones;

/*
Nota: Después del ROLLBACK, solo veremos las dos filas originales.
Operación C no se guardará y la segunda fila será restaurada.
*/
