/*
 * Objetivo: Eliminar una base de datos de PostgreSQL
 * Referencia: DROP DATABASE
 * Tipo: DDL (Data Definition Language)
 * Nivel: básico
 */

-- Eliminar base de datos simple
DROP DATABASE mi_aplicacion;

-- Eliminar solo si existe
DROP DATABASE IF EXISTS mi_aplicacion;

-- Eliminar con conexiones activas (termina conexiones primero)
DROP DATABASE IF EXISTS mi_aplicacion WITH (FORCE);

-- Listar bases de datos
\l

/*
Output esperado:
DROP DATABASE (base de datos eliminada)
*/
