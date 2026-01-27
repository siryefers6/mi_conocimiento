/*
 * Objetivo: Confirmar (guardar) una transacción
 * Referencia: COMMIT
 * Tipo: control de transacciones
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS banco (
    id SERIAL PRIMARY KEY,
    cuenta VARCHAR(100),
    saldo DECIMAL(15,2)
);

-- Insertar datos iniciales
INSERT INTO banco (cuenta, saldo)
VALUES
    ('Cuenta 1', 5000),
    ('Cuenta 2', 3000);

-- Iniciar transacción
BEGIN;

-- Transferencia de dinero
UPDATE banco SET saldo = saldo - 500 WHERE cuenta = 'Cuenta 1';
UPDATE banco SET saldo = saldo + 500 WHERE cuenta = 'Cuenta 2';

-- Ver el estado antes de COMMIT
SELECT * FROM banco;

-- COMMIT: guardar cambios permanentemente
COMMIT;

-- Los cambios son permanentes
SELECT * FROM banco;

/*
Output esperado (después de COMMIT):
 id |  cuenta  | saldo
----|----------|--------
  1 | Cuenta 1 | 4500.00
  2 | Cuenta 2 | 3500.00
*/
