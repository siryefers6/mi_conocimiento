/*
 * Objetivo: Eliminar filas de una tabla
 * Referencia: DELETE
 * Tipo: DML (Data Manipulation Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Insertar datos de prueba
INSERT INTO usuarios (nombre, email)
VALUES
    ('Juan', 'juan@email.com'),
    ('María', 'maria@email.com'),
    ('Carlos', 'carlos@email.com');

-- Eliminación simple (cuidado: elimina TODAS las filas)
-- DELETE FROM usuarios;

-- Eliminación con WHERE (segura)
DELETE FROM usuarios WHERE id = 3;

-- Verificar eliminación
SELECT * FROM usuarios;

/*
Output esperado:
 id | nombre | email
----|--------|--------------------
  1 | Juan | juan@email.com
  2 | María | maria@email.com
*/
