/*
 * Objetivo: Crear una vista (consulta guardada) en PostgreSQL
 * Referencia: CREATE VIEW
 * Tipo: DDL (Data Definition Language)
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10, 2),
    departamento VARCHAR(100)
);

-- Insertar datos de prueba
INSERT INTO empleados (nombre, salario, departamento) VALUES
('Juan', 3000, 'IT'),
('María', 3500, 'IT'),
('Carlos', 2800, 'Ventas');

-- Crear vista simple
CREATE VIEW vista_empleados AS
SELECT nombre, salario, departamento FROM empleados;

-- Crear vista con filtro
CREATE VIEW vista_empleados_it AS
SELECT nombre, salario FROM empleados WHERE departamento = 'IT';

-- Consultar la vista
SELECT * FROM vista_empleados;

-- Listar vistas
\dv

/*
Output esperado:
 nombre | salario | departamento
--------|---------|---------------
 Juan   | 3000.00 | IT
 María  | 3500.00 | IT
 Carlos | 2800.00 | Ventas
*/
