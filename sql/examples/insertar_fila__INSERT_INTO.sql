/*
 * Objetivo: Insertar una nueva fila en una tabla
 * Referencia: INSERT INTO
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

-- Insertar fila con todas las columnas
INSERT INTO usuarios (id, nombre, email, edad) 
VALUES (1, 'Juan', 'juan@email.com', 30);

-- Insertar sin especificar id (autoincremento)
INSERT INTO usuarios (nombre, email, edad)
VALUES ('María', 'maria@email.com', 28);

-- Insertar sin especificar algunas columnas
INSERT INTO usuarios (nombre, email)
VALUES ('Carlos', 'carlos@email.com');

-- Ver datos insertados
SELECT * FROM usuarios;

/*
Output esperado:
 id | nombre | email | edad
----|--------|-------|------
  1 | Juan | juan@email.com | 30
  2 | María | maria@email.com | 28
  3 | Carlos | carlos@email.com |
*/
