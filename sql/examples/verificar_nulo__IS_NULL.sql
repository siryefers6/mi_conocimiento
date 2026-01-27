/*
 * Objetivo: Verificar si un valor es NULL
 * Referencia: IS NULL
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS contactos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Insertar datos con valores NULL
INSERT INTO contactos (nombre, telefono, email)
VALUES
    ('Juan', '123456789', 'juan@email.com'),
    ('María', NULL, 'maria@email.com'),
    ('Carlos', '555555555', NULL),
    ('Ana', NULL, NULL),
    ('Luis', '777777777', 'luis@email.com');

-- IS NULL
SELECT * FROM contactos WHERE telefono IS NULL;

-- IS NOT NULL
SELECT * FROM contactos WHERE email IS NOT NULL;

-- Contar registros sin email
SELECT COUNT(*) as sin_email FROM contactos WHERE email IS NULL;

-- Múltiples condiciones con NULL
SELECT nombre FROM contactos
WHERE telefono IS NOT NULL AND email IS NOT NULL;

/*
Output esperado (IS NULL):
 id | nombre | telefono | email
----|--------|----------|----------------------
  2 | María | NULL | maria@email.com
  4 | Ana | NULL | NULL
*/
