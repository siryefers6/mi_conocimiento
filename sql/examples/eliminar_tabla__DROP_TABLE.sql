/*
 * Objetivo: Eliminar una tabla de PostgreSQL
 * Referencia: DROP TABLE
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla de prueba
CREATE TABLE temporal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Eliminar la tabla
DROP TABLE temporal;

-- Si queremos eliminar solo si existe
DROP TABLE IF EXISTS temporal;

-- Para eliminar tabla con restricciones
DROP TABLE IF EXISTS usuarios CASCADE;

/*
Output esperado:
DROP TABLE (tabla eliminada correctamente)
*/
