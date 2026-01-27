/*
 * Objetivo: Crear una vista con filtros aplicados
 * Referencia: CREATE VIEW con WHERE
 * Tipo: vista
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS transacciones (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(20),
    monto DECIMAL(10,2),
    fecha DATE
);

-- Insertar datos
INSERT INTO transacciones (tipo, monto, fecha)
VALUES
    ('Depósito', 1000, '2024-01-15'),
    ('Retiro', 500, '2024-01-16'),
    ('Depósito', 2000, '2024-01-17'),
    ('Retiro', 300, '2024-01-18');

-- Vista que solo muestra depósitos
CREATE VIEW vista_depositos AS
SELECT * FROM transacciones WHERE tipo = 'Depósito';

-- Vista que solo muestra retiros grandes
CREATE VIEW vista_retiros_mayores AS
SELECT * FROM transacciones 
WHERE tipo = 'Retiro' AND monto >= 400;

-- Usar vistas
SELECT * FROM vista_depositos;
SELECT * FROM vista_retiros_mayores;

-- Las vistas se pueden filtrar más
SELECT * FROM vista_depositos WHERE monto > 1500;

/*
Output esperado (vista_depositos):
 id | tipo | monto | fecha
----|--------|-------|----------
  1 | Depósito | 1000 | 2024-01-15
  3 | Depósito | 2000 | 2024-01-17
*/
