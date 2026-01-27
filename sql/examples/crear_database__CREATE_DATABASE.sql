/*
 * Objetivo: Crear una nueva base de datos en PostgreSQL
 * Referencia: CREATE DATABASE
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Crear base de datos simple
CREATE DATABASE mi_aplicacion;

-- Crear base de datos con propiedades específicas
CREATE DATABASE tienda
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE = 'es_ES.UTF-8'
    TEMPLATE = template0;

-- Conectarse a la base de datos (en psql)
-- \c mi_aplicacion

-- Listar bases de datos
\l

/*
Output esperado:
List of databases
   Name    | Owner | Encoding | Locale | ...
------------|-------|----------|--------|
 mi_aplicacion | postgres | UTF8 | es_ES.UTF-8 | ...
*/
