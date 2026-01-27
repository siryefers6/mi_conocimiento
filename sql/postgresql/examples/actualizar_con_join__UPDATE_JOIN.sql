/*
 * Objetivo: Actualizar registros relacionando con otra tabla
 * Referencia: UPDATE FROM (JOIN)
 * Tipo: DML (Data Manipulation Language)
 * Nivel: intermedio
 */

-- Crear tabla de departamentos
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    presupuesto DECIMAL(15,2)
);

-- Crear tabla de empleados
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento_id INT,
    salario DECIMAL(10,2)
);

-- Insertar datos
INSERT INTO departamentos (nombre, presupuesto)
VALUES ('IT', 50000), ('Ventas', 30000);

INSERT INTO empleados (nombre, departamento_id, salario)
VALUES
    ('Juan', 1, 3000),
    ('María', 1, 3500),
    ('Carlos', 2, 2800);

-- Actualizar salarios usando UPDATE FROM
UPDATE empleados
SET salario = salario * 1.15
FROM departamentos
WHERE empleados.departamento_id = departamentos.id
  AND departamentos.nombre = 'IT';

-- Ver cambios
SELECT e.nombre, d.nombre as departamento, e.salario
FROM empleados e
JOIN departamentos d ON e.departamento_id = d.id;

/*
Output esperado:
 nombre | departamento | salario
--------|--------------|--------
 Juan | IT | 3450.00
 María | IT | 4025.00
 Carlos | Ventas | 2800.00
*/
