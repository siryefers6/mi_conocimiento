/*
 * Objetivo: Insertar datos copiando desde otra tabla
 * Referencia: INSERT INTO SELECT
 * Tipo: DML (Data Manipulation Language)
 * Nivel: intermedio
 */

-- Crear tabla de origen
CREATE TABLE IF NOT EXISTS empleados_temporal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    salario DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO empleados_temporal (nombre, email, salario)
VALUES
    ('Juan', 'juan@email.com', 3000),
    ('María', 'maria@email.com', 3500),
    ('Carlos', 'carlos@email.com', 2800);

-- Crear tabla de destino
CREATE TABLE IF NOT EXISTS empleados_permanentes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    salario DECIMAL(10,2)
);

-- Insertar desde SELECT
INSERT INTO empleados_permanentes (nombre, email, salario)
SELECT nombre, email, salario FROM empleados_temporal;

-- Ver datos copiados
SELECT * FROM empleados_permanentes;

/*
Output esperado:
 id |  nombre | email | salario
----|---------|-------|--------
  1 | Juan | juan@email.com | 3000.00
  2 | María | maria@email.com | 3500.00
  3 | Carlos | carlos@email.com | 2800.00
*/
