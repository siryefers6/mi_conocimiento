/*
 * Objetivo: Actualizar registros condicionalmente con WHERE
 * Referencia: UPDATE WHERE
 * Tipo: DML (Data Manipulation Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento VARCHAR(50),
    salario DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO empleados (nombre, departamento, salario)
VALUES
    ('Juan', 'IT', 3000),
    ('María', 'IT', 3500),
    ('Carlos', 'Ventas', 2800),
    ('Ana', 'Ventas', 2500);

-- Actualizar solo empleados de IT
UPDATE empleados SET salario = salario * 1.1 WHERE departamento = 'IT';

-- Actualizar con condición AND
UPDATE empleados SET salario = 3000 WHERE departamento = 'Ventas' AND salario < 3000;

-- Ver cambios
SELECT * FROM empleados;

/*
Output esperado:
 id | nombre | departamento | salario
----|--------|--------------|--------
  1 | Juan | IT | 3300.00
  2 | María | IT | 3850.00
  3 | Carlos | Ventas | 2800.00
  4 | Ana | Ventas | 3000.00
*/
