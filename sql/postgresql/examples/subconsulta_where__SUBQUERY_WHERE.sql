/*
 * Objetivo: Usar una subconsulta en la cláusula WHERE
 * Referencia: Subconsulta en WHERE
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de empleados
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10,2),
    departamento_id INT
);

-- Insertar datos
INSERT INTO empleados (nombre, salario, departamento_id)
VALUES
    ('Juan', 3000, 1),
    ('María', 3500, 1),
    ('Carlos', 2800, 2),
    ('Ana', 2500, 2),
    ('Luis', 4000, 1);

-- Subconsulta: encontrar empleados con salario mayor al promedio
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- Subconsulta: empleados cuyo salario es igual al máximo
SELECT nombre, salario
FROM empleados
WHERE salario = (SELECT MAX(salario) FROM empleados);

-- Subconsulta: empleados del departamento con más empleados
SELECT nombre, departamento_id
FROM empleados
WHERE departamento_id = (
    SELECT departamento_id
    FROM empleados
    GROUP BY departamento_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

/*
Output esperado:
 nombre | salario
--------|--------
 María | 3500.00
 Luis | 4000.00
*/
