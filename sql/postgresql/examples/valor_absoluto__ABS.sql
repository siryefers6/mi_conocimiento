/*
 * Objetivo: Obtener el valor absoluto (sin signo)
 * Referencia: ABS()
 * Tipo: función numérica
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS transacciones (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(20),
    monto DECIMAL(10,2)
);

-- Insertar datos (negativos y positivos)
INSERT INTO transacciones (tipo, monto)
VALUES
    ('Depósito', 500.00),
    ('Retiro', -200.00),
    ('Depósito', 1000.00),
    ('Retiro', -150.00);

-- ABS() devuelve el valor absoluto
SELECT tipo, monto, ABS(monto) as monto_absoluto FROM transacciones;

-- ABS en cálculos
SELECT 
    tipo,
    ABS(monto) as cantidad,
    CASE WHEN monto > 0 THEN 'Entrada' ELSE 'Salida' END as direccion
FROM transacciones;

-- Suma de valores absolutos
SELECT SUM(ABS(monto)) as flujo_total FROM transacciones;

/*
Output esperado:
   tipo   |  monto  | monto_absoluto
-----------|---------|----------------
 Depósito | 500.00 | 500.00
 Retiro | -200.00 | 200.00
 Depósito | 1000.00 | 1000.00
 Retiro | -150.00 | 150.00
*/
