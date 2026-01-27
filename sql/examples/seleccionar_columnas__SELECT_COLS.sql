/*
 * Objetivo: Seleccionar columnas específicas
 * Referencia: SELECT col1, col2
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    salario DECIMAL(10,2),
    departamento VARCHAR(50)
);

-- Insertar datos de prueba
INSERT INTO empleados (nombre, email, telefono, salario, departamento)
VALUES
    ('Juan', 'juan@email.com', '123456789', 3000, 'IT'),
    ('María', 'maria@email.com', '987654321', 3500, 'IT'),
    ('Carlos', 'carlos@email.com', '555555555', 2800, 'Ventas');

-- Seleccionar solo algunas columnas
SELECT nombre, email FROM empleados;

-- Seleccionar múltiples columnas específicas
SELECT id, nombre, salario FROM empleados;

-- Seleccionar columnas en orden diferente
SELECT departamento, nombre, salario FROM empleados;

/*
Output esperado:
    nombre    |     email
--------------|------------------
 Juan | juan@email.com
 María | maria@email.com
 Carlos | carlos@email.com
*/
