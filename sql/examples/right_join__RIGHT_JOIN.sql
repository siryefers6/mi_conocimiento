/*
 * Objetivo: Combinar tabla derecha con coincidencias de tabla izquierda
 * Referencia: RIGHT JOIN
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de proveedores
CREATE TABLE IF NOT EXISTS proveedores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla de suministros
CREATE TABLE IF NOT EXISTS suministros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    proveedor_id INT
);

-- Insertar datos
INSERT INTO proveedores (nombre)
VALUES ('Proveedor A'), ('Proveedor B'), ('Proveedor C');

INSERT INTO suministros (nombre, proveedor_id)
VALUES
    ('Materia Prima 1', 1),
    ('Materia Prima 2', 1),
    ('Materia Prima 3', 2),
    ('Materia Prima 4', NULL);

-- RIGHT JOIN (todos de tabla derecha + coincidencias)
SELECT p.nombre as proveedor, s.nombre as suministro
FROM proveedores p
RIGHT JOIN suministros s ON p.id = s.proveedor_id;

-- RIGHT JOIN con COUNT
SELECT p.nombre, COUNT(s.id) as cantidad_suministros
FROM proveedores p
RIGHT JOIN suministros s ON p.id = s.proveedor_id
GROUP BY p.id, p.nombre;

/*
Output esperado:
 proveedor | suministro
-----------|-------------------
 Proveedor A | Materia Prima 1
 Proveedor A | Materia Prima 2
 Proveedor B | Materia Prima 3
 NULL | Materia Prima 4
*/
