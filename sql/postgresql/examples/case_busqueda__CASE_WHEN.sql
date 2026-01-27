/*
 * Objetivo: Condicional múltiple con CASE WHEN THEN
 * Referencia: CASE WHEN ... THEN ... ELSE ... END
 * Tipo: función condicional
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
    ('Juan', 2500, 'IT'),
    ('María', 3500, 'IT'),
    ('Carlos', 2000, 'Ventas'),
    ('Ana', 3000, 'Administración');

-- CASE WHEN con múltiples condiciones
SELECT 
    nombre,
    salario,
    CASE 
        WHEN salario < 2500 THEN 'Bajo'
        WHEN salario < 3000 THEN 'Medio'
        WHEN salario < 3500 THEN 'Alto'
        ELSE 'Muy Alto'
    END as categoria_salario,
    CASE 
        WHEN departamento = 'IT' THEN 'Tecnología'
        WHEN departamento = 'Ventas' THEN 'Comercial'
        ELSE 'Soporte'
    END as categoria_dept
FROM empleados;

-- CASE con AND/OR
SELECT 
    nombre,
    salario,
    CASE 
        WHEN departamento = 'IT' AND salario > 3000 THEN 'Senior IT'
        WHEN departamento = 'IT' THEN 'Junior IT'
        ELSE 'Otro'
    END as clasificacion
FROM empleados;

/*
Output esperado:
 nombre | salario | categoria_salario | categoria_dept
--------|---------|-------------------|----------------
 Juan | 2500 | Medio | Tecnología
 María | 3500 | Muy Alto | Tecnología
 Carlos | 2000 | Bajo | Comercial
 Ana | 3000 | Alto | Soporte
*/
