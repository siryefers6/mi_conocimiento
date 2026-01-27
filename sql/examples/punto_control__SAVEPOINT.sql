/*
 * Objetivo: Crear punto de control dentro de una transacción
 * Referencia: SAVEPOINT
 * Tipo: control de transacciones
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS datos (
    id SERIAL PRIMARY KEY,
    valor VARCHAR(50)
);

-- Iniciar transacción
BEGIN;

-- Punto 1
INSERT INTO datos (valor) VALUES ('Dato 1');

-- Crear savepoint
SAVEPOINT punto1;

-- Más operaciones
INSERT INTO datos (valor) VALUES ('Dato 2');
INSERT INTO datos (valor) VALUES ('Dato 3');

-- Ver datos hasta ahora
SELECT * FROM datos;

-- Si hay un error, revertir a punto1
-- ROLLBACK TO punto1;

-- O continuar y confirmar todo
COMMIT;

-- Los datos se guardaron permanentemente
SELECT * FROM datos;

/*
SAVEPOINT crea un punto intermedio en una transacción.
Con ROLLBACK TO SAVEPOINT, revertimos solo hasta ese punto.
Muy útil para manejo de errores complejo.
*/
