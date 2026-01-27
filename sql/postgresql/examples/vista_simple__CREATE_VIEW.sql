/*
 * Objetivo: Crear una vista simple
 * Referencia: CREATE VIEW
 * Tipo: vista
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10,2),
    departamento VARCHAR(50)
);

-- Insertar datos
INSERT INTO empleados (nombre, salario, departamento)
VALUES
    ('Juan', 3000, 'IT'),
    ('María', 3500, 'IT'),
    ('Carlos', 2800, 'Ventas');

-- Crear vista
CREATE VIEW vista_empleados AS
SELECT nombre, salario, departamento FROM empleados;

-- Usar la vista
SELECT * FROM vista_empleados;

-- Crear vista con alias
CREATE VIEW vista_salarios_altos AS
SELECT nombre, salario FROM empleados WHERE salario > 3000;

-- Usar segunda vista
SELECT * FROM vista_salarios_altos;

-- Ver vistas
\dv

/*
Vistas:
- Guardan consultas complejas
- Simplifica consultas repetidas
- Puede ayudar con seguridad (mostrar solo columnas específicas)
*/
