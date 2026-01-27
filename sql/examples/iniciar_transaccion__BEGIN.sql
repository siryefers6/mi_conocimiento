/*
 * Objetivo: Iniciar una transacción
 * Referencia: BEGIN
 * Tipo: control de transacciones
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS cuentas (
    id SERIAL PRIMARY KEY,
    titular VARCHAR(100),
    saldo DECIMAL(15,2)
);

-- Insertar datos iniciales
INSERT INTO cuentas (titular, saldo)
VALUES
    ('Cuenta A', 1000),
    ('Cuenta B', 500);

-- Iniciar transacción
BEGIN;

-- Operaciones dentro de la transacción
UPDATE cuentas SET saldo = saldo - 100 WHERE titular = 'Cuenta A';
UPDATE cuentas SET saldo = saldo + 100 WHERE titular = 'Cuenta B';

-- Ver cambios (dentro de transacción)
SELECT * FROM cuentas;

-- Confirmar (COMMIT) o deshacer (ROLLBACK)
-- COMMIT;  -- Para guardar
-- ROLLBACK;  -- Para deshacer

/*
Explicación:
BEGIN inicia una transacción. Los cambios se mantienen en memoria
hasta COMMIT (guardar) o ROLLBACK (deshacer).
*/
