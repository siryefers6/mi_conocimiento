/*
 * Objetivo: Modificar registros existentes en una tabla
 * Referencia: UPDATE
 * Tipo: DML (Data Manipulation Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    edad INT
);

-- Insertar datos de prueba
INSERT INTO usuarios (nombre, email, edad)
VALUES
    ('Juan', 'juan@email.com', 30),
    ('María', 'maria@email.com', 28),
    ('Carlos', 'carlos@email.com', 35);

-- Actualizar un valor específico
UPDATE usuarios SET email = 'juan.nuevo@email.com' WHERE id = 1;

-- Actualizar múltiples columnas
UPDATE usuarios SET nombre = 'Jonathan', edad = 31 WHERE id = 1;

-- Ver cambios
SELECT * FROM usuarios WHERE id = 1;

/*
Output esperado:
 id | nombre | email | edad
----|--------|-------|------
  1 | Jonathan | juan.nuevo@email.com | 31
*/
