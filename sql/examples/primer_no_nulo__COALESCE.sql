/*
 * Objetivo: Retornar el primer valor no nulo
 * Referencia: COALESCE()
 * Tipo: función condicional
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS contactos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    contacto_alterno VARCHAR(100)
);

-- Insertar datos con algunos nulos
INSERT INTO contactos (nombre, email, telefono, contacto_alterno)
VALUES
    ('Juan', 'juan@email.com', NULL, '123456789'),
    ('María', NULL, '555555555', 'maria.contacto@email.com'),
    ('Carlos', 'carlos@email.com', '777777777', NULL),
    ('Ana', NULL, NULL, 'ana@email.com');

-- COALESCE: primer no nulo
SELECT 
    nombre,
    COALESCE(email, telefono, contacto_alterno) as contacto_preferido
FROM contactos;

-- COALESCE con múltiples valores
SELECT 
    nombre,
    COALESCE(email, 'Sin email') as email,
    COALESCE(telefono, 'Sin teléfono') as telefono
FROM contactos;

-- Usar COALESCE en cálculos
SELECT 
    nombre,
    COALESCE(LENGTH(email), 0) as longitud_email,
    COALESCE(LENGTH(telefono), 0) as longitud_telefono
FROM contactos;

/*
Output esperado:
 nombre |     contacto_preferido
--------|------------------------
 Juan | juan@email.com
 María | 555555555
 Carlos | carlos@email.com
 Ana | ana@email.com
*/
