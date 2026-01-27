/*
 * Objetivo: Crear una nueva tabla en PostgreSQL
 * Referencia: CREATE TABLE
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear tabla simple con columnas y tipos de datos
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verificar que la tabla fue creada
\dt usuarios

/*
Output esperado:
Schema |  Name  | Type  | Owner
--------|--------|-------|-------
 public | usuarios | table | user
*/
