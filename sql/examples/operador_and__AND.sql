/*
 * Objetivo: Combinar múltiples condiciones con AND (todas deben cumplirse)
 * Referencia: AND
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento VARCHAR(50),
    salario DECIMAL(10,2),
    ciudad VARCHAR(50)
);

-- Insertar datos de prueba
INSERT INTO empleados (nombre, departamento, salario, ciudad)
VALUES
    ('Juan', 'IT', 3000, 'Madrid'),
    ('María', 'IT', 3500, 'Barcelona'),
    ('Carlos', 'Ventas', 2800, 'Madrid'),
    ('Ana', 'Ventas', 2500, 'Valencia');

-- AND: ambas condiciones deben ser verdaderas
SELECT * FROM empleados
WHERE departamento = 'IT' AND salario > 3200;

-- Múltiples AND
SELECT * FROM empleados
WHERE departamento = 'IT' AND salario >= 3000 AND ciudad = 'Madrid';

-- AND con valores numéricos
SELECT nombre, salario FROM empleados
WHERE salario >= 2800 AND salario <= 3500;

/*
Output esperado:
 nombre | salario
--------|--------
 María | 3500
*/
