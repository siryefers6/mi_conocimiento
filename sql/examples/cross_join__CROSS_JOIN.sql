/*
 * Objetivo: Combinar cada fila de una tabla con cada fila de otra
 * Referencia: CROSS JOIN
 * Tipo: DQL (Data Query Language)
 * Nivel: intermedio
 */

-- Crear tabla de colores
CREATE TABLE IF NOT EXISTS colores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Crear tabla de tamaños
CREATE TABLE IF NOT EXISTS tamanos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Insertar datos
INSERT INTO colores (nombre)
VALUES ('Rojo'), ('Azul'), ('Verde');

INSERT INTO tamanos (nombre)
VALUES ('Pequeño'), ('Mediano'), ('Grande');

-- CROSS JOIN (producto cartesiano)
SELECT c.nombre as color, t.nombre as tamano
FROM colores c
CROSS JOIN tamanos t
ORDER BY c.nombre, t.nombre;

-- Contar combinaciones
SELECT COUNT(*) as total_combinaciones FROM colores CROSS JOIN tamanos;

-- CROSS JOIN sin usar palabra reservada
SELECT c.nombre, t.nombre
FROM colores c, tamanos t
ORDER BY c.nombre, t.nombre;

/*
Output esperado:
 color | tamano
-------|--------
 Azul | Grande
 Azul | Mediano
 Azul | Pequeño
 Rojo | Grande
 Rojo | Mediano
 Rojo | Pequeño
 Verde | Grande
 Verde | Mediano
 Verde | Pequeño
*/
